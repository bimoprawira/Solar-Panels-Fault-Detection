# Automated Real-Time Monitoring and AI Fault Detection System for Solar Panels Using Advanced Image Detection

## Project Description
This project was designed so as to detect faulty solar panels caused by various factors such as physical damage, dusty, animal poop, covered in snow, and so on. The program is also trained to differentiate which solar panels are defective and which are not (good condition). The purpose is to avoid further deteriorations and to maintain the solar panels accurately and in a well timed manner. We believe this is aligned with the program's focus on maintaining the sustainability of clean and healthy energy (SDGs)🌼

### Problem Statement🚨

The lack of visibility into the condition of the solar panels due to factors such as dust, dirt, physical damage, and snow hampers preventive maintenance efforts, thus increasing operational costs. The solar panel maintenance team also has challenges in detecting failures or troubles in solar panels in a well-timed manner because of inefficient manual visual inspection, especially for panels located in hard-to-reach locations. This resulted in the possibility of more severe faults and decreased energy efficiency. The solar panel damage detection automation solution is present to solve the maintenance team's need to detect problems accurately and quickly, so that maintenance can be carried out more punctually and the panels function at an optimal level.

### Solution Statement💡

An automatic failure detection system uses AI (object detection) to analyze images of solar panels at frequent intervals, detecting various types of failures such as cracking, dirty areas, etc. The system generates reports showing the exact location and percentage of the failure, making it easier for technicians to carry out quick repairs and improving energy efficiency. The system generates reports showing the location and percentage of damage, enabling technicians to make quick repairs and improve energy efficiency. For landlords, the system provides real-time visibility into the condition of the panels, enabling efficient and proactive maintenance. With accurate data and historical reports, owners can minimize downtime, maximize energy production, and plan long-term investments and maintenance more effectively.

### Business Value🎯

The business solution proposed by this project is an automated system capable of detecting various types of failures in solar panels on a real-time and precise scale. Using artificial intelligence (AI) technology, the system can analyze images of solar panels and provide early warnings to the maintenance team. This program has very significant business value, including:

1.) Efficiency Improvement⚡
- <b>Early Detection</b>:
Failures can be detected before they cause a significant drop in energy production, allowing companies to take immediate corrective action.

- <b>Maintenance Optimization</b>:
Maintenance teams can focus on panels that actually need repairs, reducing unnecessary time and costs.
  
2.) Expense Savings💸
- <b>Reduced Maintenance Costs</b>:
With early detection, companies can avoid more severe failures that may require higher repair costs.
- <b>Increased Panel Lifespan</b>:
Proper and frequent maintenance can extend the life of solar panels, thereby reducing replacement costs.
  
3.) Product Quality Improvement☔
- <b>Sustained Energy Production</b>:
Well-maintained solar panels will produce energy consistently and efficiently for the concerned parties.
  
4.) Increased Customer Satisfaction📈
- <b>Energy Availability</b>:
Customers will have a more stable and reliable energy supply.
  
5.) Improving Company Reputation💌
- <b>Innovative Company Image</b>:
Companies that utilize advanced technologies such as AI will be perceived as innovative and environmentally conscious in the future.

6.) Hazard Mitigation🛡️
- <b>Preventing Fire</b>:
Any defect in the solar panels can lead to short circuits and fires. This system can help prevent such incidents.

### Sustainability (SDGs) Value🌏

![SDGs-Num7](https://github.com/user-attachments/assets/e5f5345b-fd5b-4738-968b-fff5e983b65b)
![SDGs-Num11-2](https://github.com/user-attachments/assets/1ca23072-57b0-4e5e-8b39-76c77b4a92db)
![SDGs-Num13](https://github.com/user-attachments/assets/da9445c3-f92d-46f5-aa45-c14db8260e0a)

1.) SDGs Number 7 “<b>Affordable and Clean Energy</b>”

--> The projects we build directly contribute to improving the efficiency of solar energy use. By detecting faults in solar panels in advance, the project helps ensure that solar panels operate optimally, thereby generating more and more efficient electrical energy. By increasing the efficiency of solar panels, the project can help reduce reliance on finite fossil energy sources and resulting greenhouse gas emissions. This is an important step in the transition to clean and sustainable energy.

2.) SDGs Number 11 “<b>Sustainable Cities and Communities</b>”

--> The projects we build can support sustainable urban development by supporting the increased use of renewable energy in urban environments. Well-maintained solar panels can reduce the load on conventional power grids and contribute to better air quality in cities. By increasing the use of solar energy in urban areas, this project can help reduce air and noise pollution associated with conventional power plants. In addition, it can also contribute to cities' resilience to climate change.

3.) SDGs Number 13 “<b>Climate Action</b>"

--> The projects we build directly contribute to climate change mitigation efforts. By increasing the efficiency of solar panels, the project helps reduce greenhouse gas emissions generated from conventional power plants. And, by detecting failures in solar panels earlier, the project can help ensure that investments in solar energy provide optimal returns in the long run. This is an important investment for a sustainable future.

### YOLOv8 Model Architecture🛠️<hr>

<b>Main Structures of The Main Block:</b>

![YOLOv8-Model-Architecture](https://github.com/user-attachments/assets/a536cd89-0335-405c-b28e-af3cd6be55f9)

<b>Back Structures of The Model:</b>

![YOLOv8-Back-Architecture](https://github.com/user-attachments/assets/44ddd03b-b62a-4583-8b46-da11113755c3)

## Contributor
| Full Name | Affiliation | Email | LinkedIn | Role |
| --- | --- | --- | --- | --- |
|🧏🏻‍♂️Jamilatul Muyasaroh | Startup Campus, AI Track | jamilatulmuyasarohh@gmail.com |  [link](https://id.linkedin.com/in/jamilatul-muyasaroh-1071ba300) | Team Lead |
|🧏🏻‍♀️Bimo Prawiradijaya | Startup Campus, AI Track | bimoprawiradj@gmail.com | [link](https://www.linkedin.com/in/bimopd/) | Team Member |
|🧏🏻M. Bagas Abidawaqli | Startup Campus, AI Track | abidawaqli@gmail.com | [link](https://www.linkedin.com/in/m-bagas-abidawaqli-5985a320a/) | Team Member |
|🧏🏻‍♀️Yoga Yudha Tama | Startup Campus, AI Track | yogayudhatama48@gmail.com | [link](https://www.linkedin.com/in/yoga-yudha-tama/) | Team Member |
|🧏🏻Elvizto Juan Khresnanda | Startup Campus, AI Track | elvizto.juan.k@gmail.com | [link](www.linkedin.com/in/elviztookhresnanda) | Team Member |
|🧏🏻‍♀️Yudanis Dwi Satria | Startup Campus, AI Track | yudanis16@gmail.com | [link](https://www.linkedin.com/in/yudanis-dwi-satria-142a61229/) | Team Member |
|🧏🏻‍♂️Laras Wati | Startup Campus, AI Track | xxshling27@gmail.com | [link](https://www.linkedin.com/in/laras-wati-934b58251/) | Team Member |
|👑Nicholas Dominic | Startup Campus, AI Track | nic.dominic@icloud.com | [link](https://linkedin.com/in/nicholas-dominic) | Supervisor |

## Setup
### Prerequisite Packages (Dependencies)
- nvidia-smi
- os
- IPython
- ultralytics==8.2.103
- roboflow
- ...
- ...

### Environment
| | |
| --- | --- |
| CPU | AMD Ryzen 7 5800H 8-core CPU |
| GPU | Nvidia A100 (x1) |
| ROM | 235.7 TB SSD |
| RAM Sistem | 83.5 GB |
| RAM GPU | 40 GB |
| OS | Windows 11 Version 23H2 x64-based|

## Dataset
“<b>Solar Panel Failures</b>” dataset is designed to utilize object detection techniques (computer vision). The dataset itself consists of preprocessed and annotated images (bounding box) with labels representing various types of solar panel damage (Defective, Non Defective, Dusty, Bird Drop, Physical Damage, & Snow). Where, the dataset will contain a collection of solar panel photos totaling 3650 images, with a distribution of 2585 images in the data train, 615 in the data validation, and 450 in the data test. The annotations itself total 20018 with an average of 5.5 annotations per image in each class. Details of the annotation distribution can be seen in the following figure: 

- <b>All Splits</b>

![{6C542ADE-67EF-4A7A-89F3-0500CB9E169E}](https://github.com/user-attachments/assets/3a2d8680-ec8d-4633-8f2d-4d8eccfbd988)

- <b>Train Set</b>

![{1BA51704-8E7A-4333-8B50-7FFB9C235145}](https://github.com/user-attachments/assets/5039f708-3ded-4eb8-8cfa-2d7e4ce9d01e)

- <b>Valid Set</b>

![{420D2711-794B-4D1E-BEE1-2B58F262A5D0}](https://github.com/user-attachments/assets/60677340-76ba-4db1-856c-c434e2232aea)

- <b>Test Set</b>

![{768316F7-C20A-4AD2-8D99-3F439968A537}](https://github.com/user-attachments/assets/a7d79684-4748-4b60-a7a4-50e4219bac29)

📸Sample images from several existing classes: 

- <b>Defective</b>
  
  ![Defective-Example](https://github.com/user-attachments/assets/c63320f2-f5ac-4b02-937b-99b6fdaf1fc1)
  
- <b>Non Defective</b>
  
  ![NonDefective-Example](https://github.com/user-attachments/assets/dd89f259-e4a6-4a9b-84f1-6fd4a6a6c79e)
  
- <b>Bird Drop</b>

  ![BirdDrop-Example](https://github.com/user-attachments/assets/1c42f0c7-edf4-4f54-8603-b34204c0f478)

- <b>Physical Damage</b>

  ![PhyDamage-Example](https://github.com/user-attachments/assets/01cc01e5-be96-4518-b55e-97ac6e54319e)
  
- <b>Dusty</b>

  ![Dusty-Example](https://github.com/user-attachments/assets/1d52caa2-35e3-43c2-a17e-c61fbc2fae68)
  
- <b>Snow</b>

  ![Snow-Example](https://github.com/user-attachments/assets/941d7fd9-d19d-4b99-b335-2f36a75545d6)

The version of dataset that we provide here, is a process of all the refinements of the dataset from the beginning to the end (still in the improvement stage) that we intend to use as the basis of our project. 
- Link Dataset V1: https://universe.roboflow.com/6rianstorm/solar-panel-dataset-augmentation/dataset/2  
- Link Dataset V2: https://universe.roboflow.com/6rianstorm/solar-panel-dataset-augmentation/dataset/3 
- Link Dataset V3: https://universe.roboflow.com/6rianstorm/solar-panel-dataset-augmentation/dataset/4 
- Link Dataset V4: https://universe.roboflow.com/6rianstorm/solar-panel-fault-dataset-new/dataset/1 
- Link Dataset V5: https://universe.roboflow.com/6rianstorm/solar-panel-fault-dataset-new/dataset/2
- Link Dataset V6: ...

## Results
### Model Performance
Describe all results found in your final project experiments, including hyperparameters tuning and architecture modification performances. Put it into table format. Please show pictures (of model accuracy, loss, etc.) for more clarity.

#### 1. Metrics
Inform your model validation performances, as follows:
- For classification tasks, use **Precision and Recall**.
- For object detection tasks, use **Precision and Recall**. Additionaly, you may also use **Intersection over Union (IoU)**.
- For image retrieval tasks, use **Precision and Recall**.
- For optical character recognition (OCR) tasks, use **Word Error Rate (WER) and Character Error Rate (CER)**.
- For adversarial-based generative tasks, use **Peak Signal-to-Noise Ratio (PNSR)**. Additionally, for specific GAN tasks,
  - For single-image super resolution (SISR) tasks, use **Structural Similarity Index Measure (SSIM)**.
  - For conditional image-to-image translation tasks (e.g., Pix2Pix), use **Inception Score**.

Feel free to adjust the columns in the table below.

| model | dataset_version | epoch | learning_rate | batch_size | optimizer | precision | recall | mAP50 | mAP50-95 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YOLOv5 | V2 | 100 |  0.001 | 64 | Adam | 48% | 43.9% | 0.348 | 0.237 |
| YOLOv5 | V4 | 50 | 0.001 | 128 | Adam | 34.8% | 29.4% | 0.222 | 0.13 |
| YOLOv7 | V2 | 111 | 0.001 | 16 | Adam | 57.7% | 45.5%% | 0.451 | 0.282 |
| YOLOv8s | V2 | 50 | 0.001 | 32 | Adam | 46.5% | 42.3% | 0.359 | 0.249 |
| YOLOv8s | V4 | 100 | 0.001 | 32 | Adam | 57.8% | 51% | 0.476 | 0.301 |
| YOLOv8s | V4 | 200 | 0.001 | 32 | Adam | 50.9% | 58.4% | 0.449 | 0.293 |
| YOLOv8s | V5 | 100 | 0.001 | 32 | Adam | 52.5% | 51% | 0.463 | 0.304 |
| YOLOv8s | V5 | 150 | 0.001 | 32 | Adam | 54.6% | 51.4% | 0.48 | 0.302 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

#### 2. Ablation Study
Any improvements or modifications of your base model, should be summarized in this table. Feel free to adjust the columns in the table below.

| model | layer_A | layer_B | layer_C | ... | top1_acc | top5_acc |
| --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | Conv(3x3, 64) x2 | Conv(3x3, 512) x3 | Conv(1x1, 2048) x3 | ... | 77.43% | 80.08% |
| vit_b_16 | Conv(3x3, 32) x3 | Conv(3x3, 128) x3 | Conv(1x1, 1028) x2 | ... | 72.11% | 76.84% |
| ... | ... | ... | ... | ... | ... | ... |

#### 3. Training/Validation Curve
Insert an image regarding your training and evaluation performances (especially their losses). The aim is to assess whether your model is fit, overfit, or underfit.

- <b>Confusion Matrix</b>

![ConfusionMatrix-YOLOv8s-DatasaetV5-150EPOCH](https://github.com/user-attachments/assets/4e449602-4638-48da-a7f4-27e78204ea94)

- <b>Metrics Graph</b>

![Graph-YOLOv8s-DatasetV5-150EPOCH](https://github.com/user-attachments/assets/ddd61e61-653a-4189-8d9c-46056244e93d)
 
### Testing
Show some implementations (demos) of this model. Show **at least 10 images** of how your model performs on the testing data.

![Test1](https://github.com/user-attachments/assets/d7a317ac-6c5e-4e7a-82a1-5346384403c7)

![Test2](https://github.com/user-attachments/assets/f16301f0-3262-42d9-af38-2a423b448648)

![clean jpeg](https://github.com/user-attachments/assets/610f140a-ce36-4b5e-aac6-9938914c5f57)

![dust non jpeg](https://github.com/user-attachments/assets/58598287-ef40-4c89-bff6-c3c31ac0c4b6)

![phydmg jpeg](https://github.com/user-attachments/assets/c966ea0c-5f2a-454b-abdc-e10cedccb448)

![Test3](https://github.com/user-attachments/assets/70befc49-a58c-411e-a0c6-0afcf1aceb8d)



### Deployment (Optional)
Describe and show how you deploy this project (e.g., using Streamlit or Flask), if any.

## Supporting Documents
### Presentation Deck
- Link: https://...

### Business Model Canvas
Provide a screenshot of your Business Model Canvas (BMC). Give some explanations, if necessary.

### Short Video
Provide a link to your short video, that should includes the project background and how it works.
- Link: https://...

## References
Provide all links that support this final project, i.e., papers, GitHub repositories, websites, etc.
- Link: https://...
- Link: https://...
- Link: https://...

## Additional Comments
Provide your team's additional comments or final remarks for this project. For example,
1. ...
2. ...
3. ...

## How to Cite
If you find this project useful, we'd grateful if you cite this repository:
```
@article{
...
}
```

## License
For academic and non-commercial use only.

## Acknowledgement
This project entitled <b>"YOUR PROJECT TITLE HERE"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.
