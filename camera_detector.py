import sys
import cv2

from multiprocessing import Process, Queue
from imageai.Detection import ObjectDetection


class CameraDetector:
    def __init__(self):
        # ImageAIインスタンスの初期化
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath('model/yolo-tiny.h5')
        self.detector.loadModel(detection_speed='faster')  # オプションによって制度と速度が変化する

        # openCVインスタンスの初期化
        src = 'http://210.254.207.10:80/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000'
        self.cap = cv2.VideoCapture(src)

        # キューの作成
        self.queue = Queue(maxsize=1)

        # マルチプロセスで、フレームを取得し続ける。
        self.p = Process(target=get_frame, args=(self.cap, self.queue))
        self.p.start()

    def run(self):
        """
        カメラから取得した映像に対して、推論を行う
        """

        while True:
            try:
                # キューを取得（この処理後にキューが空になる）
                bgr_img = self.queue.get()
                # ImageAIはRGBで読み込む必要があるため、BGRからRGBへ変換する。
                rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

                # ImageAIを使用して推論を行う。
                detections = self.detector.detectObjectsFromImage(input_image=rgb_img, input_type='array',
                                                                  output_type='array',
                                                                  minimum_percentage_probability=30)

                # 推論結果をディスプレイに表示する。
                cv2.imshow('screen', cv2.cvtColor(detections[0], cv2.COLOR_RGB2BGR))
                cv2.waitKey(1)

            # キーボードの「Ctrl-C」が押された場合、以下の終了処理を行う
            except (KeyboardInterrupt, ValueError):
                cv2.destroyAllWindows()
                self.cap.release()
                self.queue.close()
                self.p.terminate()
                print('Bye')
                sys.exit(0)


def get_frame(cap, queue):
    """
    フレームを取得し、キューが空の場合、
    フレームをキューに入れ続ける。
    Args:
        cap:VideoCaptureオブジェクト
        queue:キュー
    """
    while True:
        # フレームを取得する
        _, frame = cap.read()

        # キューが空の場合、キューにフレームを入れる。
        if queue.empty():
            queue.put(frame)


if __name__ == '__main__':
    c = CameraDetector()
    c.run()
