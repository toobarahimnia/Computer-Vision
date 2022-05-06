import os
import glob
# import multiprocessing
# import cv2
# import numpy as np

output_x = []
output_y = []
r = 0
def runFile(path):

    img = cv2.imread(path)
    img = cv2.resize(img, (256, 256))
    output_x.append(img)

if __name__ == '__main__':
    project = "/Users/toobarahimnia/Desktop/Project/**/Training*.jpg"  # modify this line only
    
    list = glob.glob(project, recursive=True)
    print(list[0])
    # for i in list:
    #     runFile(i)
    #     output_y.append(0)
    #     # print("0")
    #     r += 1

    # project = "/Users/apple/Desktop/Images/Jenisha/**/Training*.jpg"  # modify this line only
    # list = glob.glob(project, recursive=True)
    # for i in list:
    #     runFile(i)
    #     output_y.append(1)
    #     # print("1")
    #     r += 1

    # project = "/Users/apple/Desktop/Images/Kevin/**/Training*.jpg"  # modify this line only
    # list = glob.glob(project, recursive=True)
    # for i in list:
    #     runFile(i)
    #     output_y.append(2)
    #     # print("2")
    #     r += 1

    # project = "/Users/apple/Desktop/Images/Tooba/**/Training*.jpg"  # modify this line only
    # list = glob.glob(project, recursive=True)
    # for i in list:
    #     runFile(i)
    #     output_y.append(3)
    #     # print("3")
    #     r += 1

    # project = "/Users/apple/Desktop/Images/Tri-tin/**/Training*.jpg"  # modify this line only
    # list = glob.glob(project, recursive=True)
    # for i in list:
    #     runFile(i)
    #     output_y.append(4)
    #     # print("4")
    #     r += 1
    # print(r)

    # r = 0

    # x = np.asarray(output_x)
    # x = x.reshape(x.shape[0],-1)
    # y = np.asarray(output_y)
    # print('save')
    # np.savetxt("train_x.csv", x, delimiter=",")
    # np.savetxt("train_y.csv", y, delimiter=",")

    # output_x = []
    # output_y = []


    # project = "/Users/apple/Desktop/Images/Elsa/**/Testing*.jpg"  # modify this line only
    # list = glob.glob(project, recursive=True)
    # for i in list:
    #     runFile(i)
    #     output_y.append(0)
    #     print("0")
    #     r += 1

    # project = "/Users/apple/Desktop/Images/Jenisha/**/Testing*.jpg"  # modify this line only
    # list = glob.glob(project, recursive=True)
    # for i in list:
    #     runFile(i)
    #     output_y.append(1)
    #     print("1")
    #     r += 1

    # project = "/Users/apple/Desktop/Images/Kevin/**/Testing*.jpg"  # modify this line only
    # list = glob.glob(project, recursive=True)
    # for i in list:
    #     runFile(i)
    #     output_y.append(2)
    #     print("2")
    #     r += 1

    # project = "/Users/apple/Desktop/Images/Tooba/**/Testing*.jpg"  # modify this line only
    # list = glob.glob(project, recursive=True)
    # for i in list:
    #     runFile(i)
    #     output_y.append(3)
    #     print("3")
    #     r += 1

    # project = "/Users/apple/Desktop/Images/Tri-tin/**/testing*.jpg"  # modify this line only
    # list = glob.glob(project, recursive=True)
    # for i in list:
    #     runFile(i)
    #     output_y.append(4)
    #     print("4")
    #     r += 1

    # print(r)
    # x = np.asarray(output_x)
    # x = x.reshape(x.shape[0],-1)
    # y = np.asarray(output_y)
    # print('save')
    # np.savetxt("test_x.csv", x, delimiter=",")
    # np.savetxt("test_y.csv", y, delimiter=",")



