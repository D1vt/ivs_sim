#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:52:11 2017

@author: lracuna
"""
from vision.camera import *
from vision.plane import Plane
import autograd.numpy as np
from autograd import grad
from error_functions import geometric_distance_points, get_matrix_conditioning_number, volker_metric,calculate_A_matrix

class Gradient:
  dx1 = None
  dy1 = None
  dx2 = None
  dy2 = None
  dx3 = None
  dy3 = None
  dx4 = None
  dy4 = None
  dx5 = None
  dy5 = None

  dx1_eval = None
  dy1_eval = None

  dx2_eval = None
  dy2_eval = None

  dx3_eval = None
  dy3_eval = None

  dx4_eval = None
  dy4_eval = None

  dx5_eval = None
  dy5_eval = None

def calculate_A_matrix_autograd_Test(x1,y1,x2,y2,x3,y3,x4,y4):
  """ Calculate the A matrix for the DLT algorithm:  A.H = 0
  all coordinates are in object plane
  """

  u1 = x1*2
  v1 = x1*2

  u2 = x1*2
  v2 = x1*2

  u3 = x1*2
  v3 = x1*2

  u4 = x1*2
  v4 = x1*2


  A = np.array([    [ 0,  0, 0, -x1, -y1, -1,  v1*x1,  v1*y1,  v1],
                    [x1, y1, 1,   0,   0,  0, -u1*x1, -u1*y1, -u1],

                    [ 0,  0, 0, -x2, -y2, -1,  v2*x2,  v2*y2,  v2],
                    [x2, y2, 1,   0,   0,  0, -u2*x2, -u2*y2, -u2],

                    [ 0,  0, 0, -x3, -y3, -1,  v3*x3,  v3*y3,  v3],
                    [x3, y3, 1,   0,   0,  0, -u3*x3, -u3*y3, -u3],

                    [0,   0, 0, -x4, -y4, -1,  v4*x4,  v4*y4,  v4],
                    [x4, y4, 1,   0,   0,  0, -u4*x4, -u4*y4, -u4],
          ])
  return A


def calculate_A_matrix_autograd(x1,y1,x2,y2,x3,y3,x4,y4,P):
  """ Calculate the A matrix for the DLT algorithm:  A.H = 0
  all coordinates are in object plane
  """
  X1 = np.array([[x1],[y1],[0.],[1.]])
  X2 = np.array([[x2],[y2],[0.],[1.]])
  X3 = np.array([[x3],[y3],[0.],[1.]])
  X4 = np.array([[x4],[y4],[0.],[1.]])

  U1 = np.array(np.dot(P,X1))
  U2 = np.array(np.dot(P,X2))
  U3 = np.array(np.dot(P,X3))
  U4 = np.array(np.dot(P,X4))

  u1 = U1[0,0]/U1[2,0]
  v1 = U1[1,0]/U1[2,0]

  u2 = U2[0,0]/U2[2,0]
  v2 = U2[1,0]/U2[2,0]

  u3 = U3[0,0]/U3[2,0]
  v3 = U3[1,0]/U3[2,0]

  u4 = U4[0,0]/U4[2,0]
  v4 = U4[1,0]/U4[2,0]

  A = np.array([    [ 0,  0, 0, -x1, -y1, -1,  v1*x1,  v1*y1,  v1],
                    [x1, y1, 1,   0,   0,  0, -u1*x1, -u1*y1, -u1],

                    [ 0,  0, 0, -x2, -y2, -1,  v2*x2,  v2*y2,  v2],
                    [x2, y2, 1,   0,   0,  0, -u2*x2, -u2*y2, -u2],

                    [ 0,  0, 0, -x3, -y3, -1,  v3*x3,  v3*y3,  v3],
                    [x3, y3, 1,   0,   0,  0, -u3*x3, -u3*y3, -u3],

                    [0,   0, 0, -x4, -y4, -1,  v4*x4,  v4*y4,  v4],
                    [x4, y4, 1,   0,   0,  0, -u4*x4, -u4*y4, -u4],
          ])
  return A

def calculate_A_matrix_autograd5(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,P):
  """ Calculate the A matrix for the DLT algorithm:  A.H = 0
  all coordinates are in object plane
  """
  X1 = np.array([[x1],[y1],[0.],[1.]])
  X2 = np.array([[x2],[y2],[0.],[1.]])
  X3 = np.array([[x3],[y3],[0.],[1.]])
  X4 = np.array([[x4],[y4],[0.],[1.]])
  X5 = np.array([[x5],[y5],[0.],[1.]])

  U1 = np.array(np.dot(P,X1))
  U2 = np.array(np.dot(P,X2))
  U3 = np.array(np.dot(P,X3))
  U4 = np.array(np.dot(P,X4))
  U5 = np.array(np.dot(P,X5))

  u1 = U1[0,0]/U1[2,0]
  v1 = U1[1,0]/U1[2,0]

  u2 = U2[0,0]/U2[2,0]
  v2 = U2[1,0]/U2[2,0]

  u3 = U3[0,0]/U3[2,0]
  v3 = U3[1,0]/U3[2,0]

  u4 = U4[0,0]/U4[2,0]
  v4 = U4[1,0]/U4[2,0]

  u5 = U5[0,0]/U5[2,0]
  v5 = U5[1,0]/U5[2,0]

  A = np.array([    [ 0,  0, 0, -x1, -y1, -1,  v1*x1,  v1*y1,  v1],
                    [x1, y1, 1,   0,   0,  0, -u1*x1, -u1*y1, -u1],

                    [ 0,  0, 0, -x2, -y2, -1,  v2*x2,  v2*y2,  v2],
                    [x2, y2, 1,   0,   0,  0, -u2*x2, -u2*y2, -u2],

                    [ 0,  0, 0, -x3, -y3, -1,  v3*x3,  v3*y3,  v3],
                    [x3, y3, 1,   0,   0,  0, -u3*x3, -u3*y3, -u3],

                    [0,   0, 0, -x4, -y4, -1,  v4*x4,  v4*y4,  v4],
                    [x4, y4, 1,   0,   0,  0, -u4*x4, -u4*y4, -u4],

                    [0,   0, 0, -x5, -y5, -1,  v5*x5,  v5*y5,  v5],
                    [x5, y5, 1,   0,   0,  0, -u5*x5, -u5*y5, -u5],
          ])
  return A


def volker_metric_autograd(x1,y1,x2,y2,x3,y3,x4,y4,P):
  A = calculate_A_matrix_autograd(x1,y1,x2,y2,x3,y3,x4,y4,P)

  # nomarlize each row
  #A = A/np.linalg.norm(A,axis=1, ord = 1, keepdims=True)
  row_sums = list()
  for i in range(A.shape[0]):
    squared_sum = 0
    for j in range(A.shape[1]):
      squared_sum += np.sqrt(A[i,j]**2)
    #A[i,:] = A[i,:] / squared_sum
    row_sums.append(squared_sum)

  row_sums = np.array(row_sums).reshape(1,8)

  A = A/(row_sums.T)
  # compute the dot product
  As = np.dot(A,A.T)

  # we are interested only on the upper top triangular matrix coefficients
  metric = 0
  start = 1
  for i in range(As.shape[0]):
    for j in range(start,As.shape[0]):
      metric = metric +  As[i,j]**2
    start = start +1


  #An alternative would be to use only the coefficients which correspond
  # to different points.
  #metric = np.sqrt(np.sum(As[[0,2,4,6],[1,3,5,7]]**2))

  #X vs X
  #metric = np.sum(As[[0,0,0,2,2,4],[2,4,6,4,6,6]]**2)

  #Y vs Y
  #metric = metric + np.sum(As[[1,1,1,3,3,5],[3,5,7,5,7,7]]**2)

  return  metric

def volker_metric_autograd5(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,P):
  A = calculate_A_matrix_autograd5(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,P)

  # nomarlize each row
  #A = A/np.linalg.norm(A,axis=1, ord = 1, keepdims=True)
  row_sums = list()
  for i in range(A.shape[0]):
    squared_sum = 0
    for j in range(A.shape[1]):
      squared_sum += np.sqrt(A[i,j]**2)
    #A[i,:] = A[i,:] / squared_sum
    row_sums.append(squared_sum)

  row_sums = np.array(row_sums).reshape(1,10)

  A = A/(row_sums.T)
  # compute the dot product
  As = np.dot(A,A.T)

  # we are interested only on the upper top triangular matrix coefficients
  metric = 0
  start = 1
  for i in range(As.shape[0]):
    for j in range(start,As.shape[0]):
      metric = metric +  As[i,j]**2
    start = start +1


  #An alternative would be to use only the coefficients which correspond
  # to different points.
  #metric = np.sqrt(np.sum(As[[0,2,4,6],[1,3,5,7]]**2))

  #X vs X
  #metric = np.sum(As[[0,0,0,2,2,4],[2,4,6,4,6,6]]**2)

  #Y vs Y
  #metric = metric + np.sum(As[[1,1,1,3,3,5],[3,5,7,5,7,7]]**2)

  return  metric

def matrix_conditioning_number_autograd(x1,y1,x2,y2,x3,y3,x4,y4,P):
  A = calculate_A_matrix_autograd(x1,y1,x2,y2,x3,y3,x4,y4,P)
  #A = np.vstack([A,np.array([1,1,1,1,1,1,1,1,1])])
  #return  np.linalg.norm(A)*np.linalg.norm(np.linalg.inv(A))
  U, s, V = np.linalg.svd(A,full_matrices=False)
  return s[0]/s[-1]

def matrix_conditioning_number_autograd5(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,P):
  A = calculate_A_matrix_autograd5(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,P)

  #A = np.vstack([A,np.array([1,1,1,1,1,1,1,1,1])])
  #return  np.linalg.norm(A)*np.linalg.norm(np.linalg.inv(A))
  U, s, V = np.linalg.svd(A,full_matrices=False)
  return s[0]/s[-1]


def create_gradient():
  gradient = Gradient()
  gradient.dx1 = grad(volker_metric_autograd,0)
  gradient.dy1 = grad(volker_metric_autograd,1)

  gradient.dx2 = grad(volker_metric_autograd,2)
  gradient.dy2 = grad(volker_metric_autograd,3)

  gradient.dx3 = grad(volker_metric_autograd,4)
  gradient.dy3 = grad(volker_metric_autograd,5)

  gradient.dx4 = grad(volker_metric_autograd,6)
  gradient.dy4 = grad(volker_metric_autograd,7)
  return gradient



def create_gradient1():
  gradient = Gradient()
  gradient.dx1 = grad(matrix_conditioning_number_autograd,0)
  gradient.dy1 = grad(matrix_conditioning_number_autograd,1)

  gradient.dx2 = grad(matrix_conditioning_number_autograd,2)
  gradient.dy2 = grad(matrix_conditioning_number_autograd,3)

  gradient.dx3 = grad(matrix_conditioning_number_autograd,4)
  gradient.dy3 = grad(matrix_conditioning_number_autograd,5)

  gradient.dx4 = grad(matrix_conditioning_number_autograd,6)
  gradient.dy4 = grad(matrix_conditioning_number_autograd,7)
  return gradient

def create_gradient5():
  gradient = Gradient()
  gradient.dx1 = grad(matrix_conditioning_number_autograd5,0)
  gradient.dy1 = grad(matrix_conditioning_number_autograd5,1)

  gradient.dx2 = grad(matrix_conditioning_number_autograd5,2)
  gradient.dy2 = grad(matrix_conditioning_number_autograd5,3)

  gradient.dx3 = grad(matrix_conditioning_number_autograd5,4)
  gradient.dy3 = grad(matrix_conditioning_number_autograd5,5)

  gradient.dx4 = grad(matrix_conditioning_number_autograd5,6)
  gradient.dy4 = grad(matrix_conditioning_number_autograd5,7)

  gradient.dx4 = grad(matrix_conditioning_number_autograd5,6)
  gradient.dy4 = grad(matrix_conditioning_number_autograd5,7)

  gradient.dx5 = grad(matrix_conditioning_number_autograd5,8)
  gradient.dy5 = grad(matrix_conditioning_number_autograd5,9)
  return gradient


def extract_objectpoints_vars(objectPoints):
  x1 = objectPoints[0,0]
  y1 = objectPoints[1,0]

  x2 = objectPoints[0,1]
  y2 = objectPoints[1,1]

  x3 = objectPoints[0,2]
  y3 = objectPoints[1,2]

  x4 = objectPoints[0,3]
  y4 = objectPoints[1,3]

  return x1,y1,x2,y2,x3,y3,x4,y4

def extract_objectpoints_vars5(objectPoints):
  x1 = objectPoints[0,0]
  y1 = objectPoints[1,0]

  x2 = objectPoints[0,1]
  y2 = objectPoints[1,1]

  x3 = objectPoints[0,2]
  y3 = objectPoints[1,2]

  x4 = objectPoints[0,3]
  y4 = objectPoints[1,3]

  x5 = objectPoints[0,4]
  y5 = objectPoints[1,4]

  return x1,y1,x2,y2,x3,y3,x4,y4,x5,y5

def evaluate_gradient(gradient, objectPoints, P):
  x1,y1,x2,y2,x3,y3,x4,y4 = extract_objectpoints_vars(objectPoints)
  gradient.dx1_eval = gradient.dx1(x1,y1,x2,y2,x3,y3,x4,y4, P)
  gradient.dy1_eval = gradient.dy1(x1,y1,x2,y2,x3,y3,x4,y4, P)

  gradient.dx2_eval = gradient.dx2(x1,y1,x2,y2,x3,y3,x4,y4, P)
  gradient.dy2_eval = gradient.dy2(x1,y1,x2,y2,x3,y3,x4,y4, P)

  gradient.dx3_eval = gradient.dx3(x1,y1,x2,y2,x3,y3,x4,y4, P)
  gradient.dy3_eval = gradient.dy3(x1,y1,x2,y2,x3,y3,x4,y4, P)

  gradient.dx4_eval = gradient.dx4(x1,y1,x2,y2,x3,y3,x4,y4, P)
  gradient.dy4_eval = gradient.dy4(x1,y1,x2,y2,x3,y3,x4,y4, P)

  return gradient

def evaluate_gradient5(gradient, objectPoints, P):
  x1,y1,x2,y2,x3,y3,x4,y4,x5,y5 = extract_objectpoints_vars5(objectPoints)
  gradient.dx1_eval = gradient.dx1(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)
  gradient.dy1_eval = gradient.dy1(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)

  gradient.dx2_eval = gradient.dx2(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)
  gradient.dy2_eval = gradient.dy2(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)

  gradient.dx3_eval = gradient.dx3(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)
  gradient.dy3_eval = gradient.dy3(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)

  gradient.dx4_eval = gradient.dx4(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)
  gradient.dy4_eval = gradient.dy4(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)

  gradient.dx5_eval = gradient.dx5(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)
  gradient.dy5_eval = gradient.dy5(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5, P)

  return gradient

def normalize_gradient5(gradient):
  maximum = np.max(np.abs([gradient.dx1_eval,
                gradient.dy1_eval,

                gradient.dx2_eval,
                gradient.dy2_eval,

                gradient.dx3_eval,
                gradient.dy3_eval,

                gradient.dx4_eval,
                gradient.dy4_eval,

                gradient.dx5_eval,
                gradient.dy5_eval]))

  gradient.dx1_eval /= maximum
  gradient.dy1_eval /= maximum

  gradient.dx2_eval /= maximum
  gradient.dy2_eval /= maximum

  gradient.dx3_eval /= maximum
  gradient.dy3_eval /= maximum

  gradient.dx4_eval /= maximum
  gradient.dy4_eval /= maximum

  gradient.dx5_eval /= maximum
  gradient.dy5_eval /= maximum



#  gradient.dx1_eval = np.sign(gradient.dx1_eval)*(np.random.rand(1)[0])*0.01
#  gradient.dy1_eval = np.sign(gradient.dy1_eval)*(np.random.rand(1)[0])*0.01
#
#  gradient.dx2_eval = np.sign(gradient.dx2_eval)*(np.random.rand(1)[0])*0.01
#  gradient.dy2_eval = np.sign(gradient.dy2_eval)*(np.random.rand(1)[0])*0.01
#
#  gradient.dx3_eval = np.sign(gradient.dx3_eval)*(np.random.rand(1)[0])*0.01
#  gradient.dy3_eval = np.sign(gradient.dy3_eval)*(np.random.rand(1)[0])*0.01
#
#  gradient.dx4_eval = np.sign(gradient.dx4_eval)*(np.random.rand(1)[0])*0.01
#  gradient.dy4_eval = np.sign(gradient.dy4_eval)*(np.random.rand(1)[0])*0.01
#
#  gradient.dx5_eval = np.sign(gradient.dx5_eval)*(np.random.rand(1)[0])*0.01
#  gradient.dy5_eval = np.sign(gradient.dy5_eval)*(np.random.rand(1)[0])*0.01
  return gradient





def update_points(alpha, gradient, objectPoints, limit=0.15):
  op = np.copy(objectPoints)
  op[0,0] += - gradient.dx1_eval*alpha
  op[1,0] += - gradient.dy1_eval*alpha

  op[0,1] += - gradient.dx2_eval*alpha
  op[1,1] += - gradient.dy2_eval*alpha

  op[0,2] += - gradient.dx3_eval*alpha
  op[1,2] += - gradient.dy3_eval*alpha

  op[0,3] += - gradient.dx4_eval*alpha
  op[1,3] += - gradient.dy4_eval*alpha

  op[0:3,:] = np.clip(op[0:3,:], -limit, limit)
  return op



def update_points5(alpha, gradient, objectPoints, limit=0.15):
  op = np.copy(objectPoints)
  op[0,0] += - gradient.dx1_eval*alpha
  op[1,0] += - gradient.dy1_eval*alpha

  op[0,1] += - gradient.dx2_eval*alpha
  op[1,1] += - gradient.dy2_eval*alpha

  op[0,2] += - gradient.dx3_eval*alpha
  op[1,2] += - gradient.dy3_eval*alpha

  op[0,3] += - gradient.dx4_eval*alpha
  op[1,3] += - gradient.dy4_eval*alpha

  op[0,4] += - gradient.dx5_eval*alpha
  op[1,4] += - gradient.dy5_eval*alpha

  #op[0:3,:] = np.clip(op[0:3,:], -limit, limit)
  return op



def test():

  ## CREATE A SIMULATED CAMERA
  cam = Camera()
  fx = fy =  800
  cx = 640
  cy = 480
  cam.set_K(fx,fy,cx,cy)
  cam.img_width = 1280
  cam.img_height = 960

  ## DEFINE CAMERA POSE LOOKING STRAIGTH DOWN INTO THE PLANE MODEL
  cam.set_R_axisAngle(1.0,  1.0,  0.0, np.deg2rad(165.0))
  cam_world = np.array([0.0,-0.2,1,1]).T
  cam_t = np.dot(cam.R,-cam_world)
  cam.set_t(cam_t[0], cam_t[1],  cam_t[2])
  cam.set_P()
  o_points = np.array([[1,-1,1,-1],[1,1,-1,-1],[0,0,0,0],[1,1,1,1]])
  i_points = cam.project(o_points)
  Anormal = calculate_A_matrix(o_points[[0,1,3],:],i_points)
  Aautograd = calculate_A_matrix_autograd(1,1,-1,1,1,-1,-1,-1,cam.P)
  print np.allclose(Anormal,Aautograd)


  metric_autograd = volker_metric_autograd(1,1,-1,1,1,-1,-1,-1,np.array(cam.P))

  metric_normal = volker_metric(Anormal)

  print metric_normal,metric_autograd

  f_der_x1 = grad(calculate_A_matrix_autograd_Test,0)
  print f_der_x1(1,1,-1,1,1,-1,-1,-1)

  f_der_x1 = grad(volker_metric_autograd,1)
  print f_der_x1(0.1,0.1,-0.1,0.1,0.1,-0.1,-0.1,-0.1,np.array(cam.P))


## CREATE A SIMULATED CAMERA
cam = Camera()
fx = fy =  800
cx = 640
cy = 480
cam.set_K(fx,fy,cx,cy)
cam.img_width = 1280
cam.img_height = 960

## DEFINE CAMERA POSE LOOKING STRAIGTH DOWN INTO THE PLANE MODEL
cam.set_R_axisAngle(1.0,  1.0,  0.0, np.deg2rad(165.0))
cam_world = np.array([0.0,-0.2,1,1]).T
cam_t = np.dot(cam.R,-cam_world)
cam.set_t(cam_t[0], cam_t[1],  cam_t[2])
cam.set_P()

pl =  Plane(origin=np.array([0, 0, 0]), normal = np.array([0, 0, 1]), size=(0.3,0.3), n = (2,2))
pl.random(n =4, r = 0.01, min_sep = 0.01)



## CREATE A SET OF IMAGE POINTS FOR VALIDATION OF THE HOMOGRAPHY ESTIMATION
validation_plane =  Plane(origin=np.array([0, 0, 0]), normal = np.array([0, 0, 1]), size=(0.3,0.3), n = (4,4))
validation_plane.uniform()
x = np.linspace(10, cam.img_width-10, 10)
y = np.linspace(10, cam.img_height-10, 10)
xx,yy = np.meshgrid(x,y)
validation_imagePoints = np.array([xx.ravel(),yy.ravel(), np.ones_like(yy.ravel())])


gradient = create_gradient1()



objectPoints_des = pl.get_points()
imagePoints_des = np.array(cam.project(objectPoints_des, False))
objectPoints_list = list()
imagePoints_list = list()
new_objectPoints = objectPoints_des
alpha = 0.0000000001
for i in range(10000):
  objectPoints = np.copy(new_objectPoints)
  gradient = evaluate_gradient(gradient,objectPoints, np.array(cam.P))
  #gradient = normalize_gradient(gradient)

  new_objectPoints = update_points(alpha, gradient, objectPoints)
  new_imagePoints = np.array(cam.project(new_objectPoints, False))

  objectPoints_list.append(new_objectPoints)
  imagePoints_list.append(new_imagePoints)
  plt.ion()
  #plt.cla()
  plt.figure('Image Points')
  if i==0:
    plt.cla()
    cam.plot_plane(pl)
    plt.plot(imagePoints_des[0],imagePoints_des[1],'x',color = 'black',)
  plt.plot(new_imagePoints[0],new_imagePoints[1],'.',color = 'blue',)

  plt.xlim(0,1280)
  plt.ylim(0,960)
  plt.gca().invert_yaxis()
  plt.pause(0.01)

  Xo = np.copy(new_objectPoints[[0,1,3],:]) #without the z coordinate (plane)
  Xi = np.copy(new_imagePoints)
  Aideal = calculate_A_matrix(Xo, Xi)

  #x1,y1,x2,y2,x3,y3,x4,y4,x5,y5 = extract_objectpoints_vars5(new_objectPoints)
  #mat_cond = matrix_conditioning_number_autograd5(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,np.array(cam.P))

  x1,y1,x2,y2,x3,y3,x4,y4 = extract_objectpoints_vars(new_objectPoints)
  mat_cond = matrix_conditioning_number_autograd(x1,y1,x2,y2,x3,y3,x4,y4,np.array(cam.P))

  volkerMetric = volker_metric(Aideal)

  alpha += 0.0000000001

  print "Iteration: ", i
  print "Mat cond:", mat_cond
  print "Volker Metric:", volkerMetric
  print "dx1,dy1 :", gradient.dx1_eval,gradient.dy1_eval
  print "dx2,dy2 :", gradient.dx2_eval,gradient.dy2_eval
  print "dx3,dy3 :", gradient.dx3_eval,gradient.dy3_eval
  print "dx4,dy4 :", gradient.dx4_eval,gradient.dy4_eval
  print "dx5,dy5 :", gradient.dx5_eval,gradient.dy5_eval
  print "------------------------------------------------------"
