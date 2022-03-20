<center> 
    <h1>
        AI HACKATON
    </h1> 
</center>

------

<center> 
    <h3>
        BRAIN NTNU x Microsoft x HUB Ocean
    </h3> 
</center>

---

<center> 
    <h2>
        Objektdeteksjon av korallrev ved hjelp av Sentinel-satelittbilder
    </h2> 
</center>

#### av Martin Johannes Nilsen, Ole Jonas Liahagen, Zaim Imran og Salar Adel


## Introduksjon
Hva har blitt gjort:
- Hentet bilder fra Planetary HUB
- Klassifisering av data med Azure ML assisted labeling
- Eksporter som COCO, oversett til YOLO
- Bilder og labels på riktig format
- Nedskalering av bilder, 343px ganske spesiell oppløsning så nå oppløsning på 320px (32-gangen for kernel av 32px i YOLO)
- Trening av YOLOv5 på denne


## Hvordan trene YOLOv5-nettverket
Eksempel på trening:
```
python train.py --img 320 --batch 16 --epochs 80 --data dataset.yaml --weights yolov5s.pt --optimizer Adam --cache
```

* **img**: define input image size
* **batch**: determine batch size
* **epochs**: define the number of training epochs.
* **data**: Our dataset locaiton is saved in the dataset.location
* **weights**: specify a path to weights to start transfer learning from. Here we choose the generic COCO pretrained checkpoint.
* **optimizer**: Select optimizer {SGD, Adam, AdamW}
* **cache**: cache images for faster training


## Detektering med trente vekter
```
python detect.py --weights runs/train/exp/weights/best.pt --img 320 --conf 0.1 --source {dataset.location}/test/images
```
* **weights**: specify path of weights as .pt-file
* **img**: define input image size
* **conf**: confidence needed for classification
* **source**: define path to test images


