import sys
import cv2

from multiprocessing import Process, Queue


class CameraDetector:
    def __init__(self):

        # オブジェクト初期化
        self.cap = cv2.VideoCapture(
            'http://210.254.207.10:80/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000')

        # マルチプロセスで、フレームを取得し続ける。
        self.p = Process(target=get_frame, args=(self.cap,))
        self.p.start()
        pass

    def run(self):
        """
        カメラから取得した映像に対して、推論を行う
        """

        while True:
            try:
                # キューを取得（この処理後にキューが空になる）
                frame = queue.get()

                cv2.imshow('frame', frame)
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
    while True:
        # フレームを取得する
        _, frame = cap.read()

        # キューが空の場合、キューにフレームを入れる。
        if queue.empty():
            queue.put(frame)


if __name__ == '__main__':
    c = CameraDetector()
    c.run()
