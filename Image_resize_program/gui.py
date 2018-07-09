import sys
import cv2
import time


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QMessageBox, QInputDialog
from PyQt5.QtWidgets import QFileDialog
import numpy as np

from other_algo import algorithm_3, algorithm_4, algorithm_5
from work import work_work, work_work_progress
from algo import one_d, two_d, my_algorithm


class window(QMainWindow):
    def __init__(self):
        # render gui windows and set its size and toolbars
        super(window, self).__init__()
        self.setGeometry(50, 50, 1100, 600)  # x= 800 y = 500
        self.setWindowTitle('Seam Carving GUI')

        gui_open_file = QAction('&Open File', self)
        gui_open_file.triggered.connect(self.file_open)

        self.statusBar()

        gui_main_screen = self.menuBar()
        gui_toolbar = gui_main_screen.addMenu('&File')
        gui_toolbar.addAction(gui_open_file)

        self.home()

    def only_result(self):
        # Handle button open image file from toolbar

        choice = QMessageBox.question(self, 'Seam direction',
                                      "Seam direction: Yes for horizontally, No for vertically, default vertically",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        i, user_response = QInputDialog.getInt(self, "default 50, max 500", "Number of seams to be removed:", 50, 0, 500,
                                           1)
        # beach pick 50 and vertical
        if user_response:
            seams_per_iter = i
        else:
            seams_per_iter = 50

        if choice == QMessageBox.Yes:
            direction = 'horizontal'

        else:
            direction = 'vertical'

        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

        the_image = str(name)

        print("location " + the_image)

        open_img = cv2.imread(the_image, 1)

        i, user_response = QInputDialog.getInt(self, " Algorithm type(Default 2) ", "Which Algorithm type (1-5)", 2, 1,
                                           5, 1)

        # beach pick 50 and vertical
        if user_response:
            algorithm_type = i
        else:
            algorithm_type = 2

        final_result = work_work(open_img, direction, seams_per_iter, algorithm_type)

        choice = QMessageBox.question(self, 'Save img',
                                      "Save file afterword?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:

            i, user_response = QInputDialog.getText(self, "default name result", "Enter a name of the image")

            # beach pick 50 and vertical
            if user_response:
                user_naming = i
            else:
                   user_naming = "result"

            print(user_naming)

            i, user_response = QInputDialog.getText(self, "Save as PNG OR JPG? (Default png) ", "Enter a type of the image")

            # beach pick 50 and vertical
            if user_response:
                img_type = i
            else:
                img_type = "png"

            user_naming = str(user_naming) + "." + img_type

            # Before converting pic to uint8, you need to multiply it by 255 to get the correct range.
            # https://stackoverflow.com/questions/19239381/pyplot-imsave-saves-image-correctly-but-cv2-imwrite-saved-the-same-image-as
            cv2.imwrite(user_naming, (final_result * 255).astype(np.uint8))
            print(user_naming)
            cv2.imshow('Result', final_result)

        else:

            cv2.imshow("Result ", final_result)  # for visualization




    def file_open(self):
        # Handle button open image file from toolbar

        choice = QMessageBox.question(self, 'Seam direction',
                                      "Seam direction: Yes for horizontally, No for vertically, default vertically",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        i, user_response = QInputDialog.getInt(self, "default 50, max 500", "Number of seams to be removed:", 50, 0, 500,
                                           1)
        # beach pick 50 and vertical
        if user_response:
            seams_per_iter = i
        else:
            seams_per_iter = 50

        if choice == QMessageBox.Yes:
            direction = 'horizontal'

        else:
            direction = 'vertical'

        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

        the_image = str(name)

        print("location " + the_image)

        open_img = cv2.imread(the_image, 1)

        i, user_response = QInputDialog.getInt(self, " Algorithm type(Default 2) ", "Which Algorithm type (1-5)", 2, 1,
                                               5, 1)

        # beach pick 50 and vertical
        if user_response:
            algorithm_type = i
        else:
            algorithm_type = 2

        final_result = work_work(open_img, direction, seams_per_iter, algorithm_type)

        choice = QMessageBox.question(self, 'Save img',
                                      "Save file afterword?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:

            i, user_response = QInputDialog.getText(self, "default name result", "Enter a name of the image")

            # beach pick 50 and vertical
            if user_response:
                user_naming = i
            else:
                user_naming = "result"

            print(user_naming)

            i, user_response = QInputDialog.getText(self, "Save as PNG OR JPG? (Default png) ", "Enter a type of the image")

            # beach pick 50 and vertical
            if user_response:
                img_type = i
            else:
                img_type = "png"

            user_naming = str(user_naming) + "." + img_type

            # Before converting pic to uint8, you need to multiply it by 255 to get the correct range.
            # https://stackoverflow.com/questions/19239381/pyplot-imsave-saves-image-correctly-but-cv2-imwrite-saved-the-same-image-as
            cv2.imwrite(user_naming, (final_result * 255).astype(np.uint8))
            print(user_naming)
            cv2.imshow('Result', final_result)
            cv2.imshow('Original Image', open_img)
        else:

            cv2.imshow("Result ", final_result)  # for visualization
            cv2.imshow('Original Image', open_img)

    def home(self):
        # render gui home
        btn = QPushButton('Original', self)
        btn.clicked.connect(self.open_ori_img)
        btn.setFixedWidth(100)
        btn.setFixedHeight(100)
        btn.move(0, 250)  # x = 0 y = 100

        btn = QPushButton('Gray scale', self)
        btn.clicked.connect(self.open_gray_img)
        btn.setFixedWidth(100)
        btn.setFixedHeight(100)
        btn.move(200, 250)  # x = 0 y = 100

        btn = QPushButton('Energy map', self)
        btn.clicked.connect(self.open_energy_img)
        btn.setFixedWidth(100)
        btn.setFixedHeight(100)
        btn.move(400, 250)  # x = 0 y = 100

        btn = QPushButton('Result', self)
        btn.clicked.connect(self.only_result)
        btn.setFixedWidth(100)
        btn.setFixedHeight(100)
        btn.move(600, 250)  # x = 0 y = 100

        btn = QPushButton('Progress', self)
        btn.clicked.connect(self.see_seam_progress)
        btn.setFixedWidth(100)
        btn.setFixedHeight(100)
        btn.move(800, 250)  # x = 0 y = 100

        btn = QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.setFixedWidth(100)
        btn.setFixedHeight(100)
        btn.move(1000, 250)  # x = 0 y = 100

        btn = QPushButton('Compare', self)
        btn.clicked.connect(self.check_performance)
        btn.setFixedWidth(100)
        btn.setFixedHeight(100)
        btn.move(1000, 350)  # x = 0 y = 100

        self.show()

    def see_seam_progress(self):
        # Handle button click progress/steps

        choice = QMessageBox.question(self, 'Seam direction',
                                      "Seam direction: Yes for horizontally, No for vertically, default vertically",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        i, okPressed = QInputDialog.getInt(self, "default 50, max 500", "Number of seams to be removed:", 50, 0, 500,
                                           1)
        # beach pick 50 and vertical
        if okPressed:
            seams_per_iter = i
        else:
            seams_per_iter = 50

        if choice == QMessageBox.Yes:
            direction = 'horizontal'

        else:
            direction = 'vertical'

        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

        the_image = str(name)

        open_img = cv2.imread(the_image, 1)

        i, user_response = QInputDialog.getInt(self, " Algorithm type(Default 2) ", "Which Algorithm type (1-5)", 2, 1,
                                               5, 1)

        # beach pick 50 and vertical
        if okPressed:
            algo_type = i
        else:
            algo_type = 2

        work_work_progress(open_img, direction, seams_per_iter, algo_type)

    def close_application(self):
        # Handle button click quit/exit

        choice = QMessageBox.question(self, 'Message', "Close program now? All unsaved changes will be lost",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)

        if choice == QMessageBox.Yes:

            sys.exit()
        else:
            pass
    def check_performance(self):

        checking = cv2.imread("/Users/dev/Desktop/CSE_534_CODE/cse534_code/File5.jpg", 1)
        start_time = time.time()
        my_algorithm(checking,3)
        print("algorithm 3 took " + str((time.time() - start_time)))

        start_time = time.time()
        my_algorithm(checking,1)
        print("algorithm 1 took " + str((time.time() - start_time)))

        start_time = time.time()
        my_algorithm(checking,2)
        print("algorithm 2 took " + str((time.time() - start_time)))

        start_time = time.time()
        my_algorithm(checking,4)
        print("algorithm 4 took " + str((time.time() - start_time)))

        start_time = time.time()
        my_algorithm(checking,5)
        print("algorithm 5 took " + str((time.time() - start_time)))




    def open_ori_img(self):
        # Handle button click original image

        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

        the_image = str(name)

        open_img = cv2.imread(the_image, 1)

        cv2.imshow('Button showed Original Image', open_img)

    def open_gray_img(self):
        # Handle button click gray image

        choice = QMessageBox.question(self, 'Save img',
                                      "Save file afterword?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:

            i, okPressed = QInputDialog.getText(self, "default name result", "Enter a name of the image")

            # beach pick 50 and vertical
            if okPressed:
                user_nameing = i
            else:
                user_nameing = "result"

            print(user_nameing)

            i, okPressed = QInputDialog.getText(self, "Save as PNG OR JPG? (Default png) ", "Enter a type of the image")

            # beach pick 50 and vertical
            if okPressed:
                img_type = i
            else:
                img_type = "png"

            name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

            the_image = str(name)

            user_nameing = str(user_nameing) + "." + img_type

            open_img = cv2.imread(the_image, 0)
            cv2.imwrite(user_nameing, open_img)  # multiple to convert 0-1 to 0-255
            cv2.imshow('Button showed gray Image', open_img)

        else:

            name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

            the_image = str(name)

            open_img = cv2.imread(the_image, 0)

            cv2.imshow('Button showed gray Image', open_img)

    def open_energy_img(self):
        # Handle button click energy
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)

        the_image = str(name)

        open_img = cv2.imread(the_image, 0)

        img_b = cv2.GaussianBlur(open_img, (3, 3), 0)   # blur it
        x = np.array((-1, 0, 1, -2, 0, 2, -1, 0, 1))
        y = np.array((-1, -2, -1, 0, 0, 0, 1, 2, 1))
        gx = np.reshape(x, [3, 3])  # gradient in x
        gy = np.reshape(y, [3, 3])  # gradient in y

        img_b = img_b.astype("float")

        ggx = two_d(img_b, gx)
        ggy = two_d(img_b, gy)

        g = np.sqrt(ggx * ggx + ggy * ggy)
        g = g.max() * g

        # also show algo 1 enery map:

        the_image = str(name)

        open_img = cv2.imread(the_image, 0)

        img_b = cv2.GaussianBlur(open_img, (3, 3), 0)  # reduce high frequency noise

        gx1 = np.array((1, 2, 1))  # vertical
        gx2 = np.array((-1, 0, 1))
        gy1 = np.array((-1, 0, 1))  # vertical
        gy2 = np.array((1, 2, 1))
        gx1 = gx1.reshape(3, 1)
        gy1 = gy1.reshape(3, 1)

        b = one_d(img_b, gy1, gy2)
        a = one_d(img_b, gx1, gx2)
        c = np.sqrt(a * a + b * b)

        cv2.imshow('Button showed energy Image algo2', g)  # Algorithm based on 2D Convolution
        cv2.imshow('Button showed energy Image algo1', c)  # Algorithm based on 1D Convolution

        cv2.imshow('Button showed energy Image algo3', algorithm_3(open_img))
        cv2.imshow('Button showed energy Image algo4', algorithm_4(open_img))
        cv2.imshow('Button showed energy Image algo5', algorithm_5(open_img))


if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
