from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, serializers, status
from rest_framework.generics import GenericAPIView

# Create your views here.
from rest_framework.response import Response
import client

class PeopleDetectSerializer(serializers.Serializer):
    image = serializers.ImageField()


class PeopleDetectClassify(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PeopleDetectSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = serializer.validated_data.get('image')
        response = client.run(weights='yolov5s.pt',  # model.pt path(s)
                                source=image,  # file/dir/URL/glob, 0 for webcam
                                data='yolov5/data/coco128.yaml',  # dataset.yaml path
                                imgsz=(640, 640),  # inference size (height, width)
                                conf_thres=0.4,  # confidence threshold
                                iou_thres=0.45,  # NMS IOU threshold
                                max_det=1000,  # maximum detections per image
                                device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
                                view_img=False,  # show results
                                save_txt=False,  # save results to *.txt
                                save_conf=False,  # save confidences in --save-txt labels
                                save_crop=False,  # save cropped prediction boxes
                                nosave=False,  # do not save images/videos
                                classes=0,  # filter by class: --class 0, or --class 0 2 3
                                agnostic_nms=False,  # class-agnostic NMS
                                augment=False,  # augmented inference
                                visualize=False,  # visualize features
                                update=False,  # update all models
                                project='runs/detect',  # save results to project/name
                                name='exp',  # save results to project/name
                                exist_ok=False,  # existing project/name ok, do not increment
                                line_thickness=3,  # bounding box thickness (pixels)
                                hide_labels=False,  # hide labels
                                hide_conf=False,  # hide confidences
                                half=False,  # use FP16 half-precision inference
                                dnn=True,  # use OpenCV DNN for ONNX inference
                                )
        return Response(response, status=status.HTTP_200_OK)