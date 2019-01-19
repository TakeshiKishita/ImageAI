import sys
import cv2

from multiprocessing import Process, Queue
from imageai.Detection import ObjectDetection


class CameraDetector:
    def __init__(self):
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath('model/yolo-tiny.h5')
        self.detector.loadModel()

        # オブジェクト初期化
        self.cap = cv2.VideoCapture(
            'http://210.254.207.10:80/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000')

        # マルチプロセスで、フレームを取得し続ける。
        self.p = Process(target=get_frame, args=(self.cap,))
        self.p.start()

    def run(self):
        """
        カメラから取得した映像に対して、推論を行う
        """
        global queue

        while True:
            try:
                # キューを取得（この処理後にキューが空になる）
                bgr_img = queue.get()
                # ImageAIはRGBで読み込む必要があるため、BGRからRGBへ変換する。
                rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

                detections = self.detector.detectObjectsFromImage(input_image=rgb_img, input_type='array',
                                                                  output_type='array',
                                                                  minimum_percentage_probability=30)

                cv2.imshow('frame', detections[0])
                cv2.waitKey(1)

            # キーボードの「Ctrl-C」が押された場合、以下の終了処理を行う
            except KeyboardInterrupt:
                self.cap.release()
                cv2.destroyAllWindows()
                self.p.terminate()
                sys.exit()


# キューの作成
queue = Queue()


def get_frame(cap):
    """
    フレームを取得し、キューが空の場合、
    フレームをキューに入れ続ける。
    Args:
        cap:

    Returns:

    """
    global queue
    while True:
        # フレームを取得する
        _, frame = cap.read()

        # キューが空の場合、キューにフレームを入れる。
        if queue.empty():
            queue.put(frame)


if __name__ == '__main__':
    c = CameraDetector()
    c.run()
