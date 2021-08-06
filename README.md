<!--
*** This README markdown is built from the following repo
*** https://github.com/othneildrew/Best-README-Template
-->



<!-- PROJECT SHIELDS -->
<!--
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />


  <h3 align="center">Gesture Volume Controller</h3>

  <p align="left">
    Control master or app specified volume using your hand gestures
    <br />
    <a href="https://github.com/SamirGouda/Gesture_Volume_Control_Project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

In this project we will build a volume controller using Python, OpenCV, pycaw

We can divide the project into the following tasks:
* Capture frames from webcam using `OpenCV` framework
* Detect hand landmarks using google `Mediapipe` package
* `hand_tracking_module` tracks landmarks of both index and thumb fingers 
* Using these landmarks, and the `audio_controller` module controls the volume either master or app specific


### Built With

frameworks used in building this project

* [OpenCV](https://opencv.org)
* [MediaPipe](https://mediapipe.dev)
* [pycaw](https://github.com/AndreMiras/pycaw)


<!-- GETTING STARTED -->
## Getting Started

You need to install the following dependencies in order to run the project
### Dependencies
- OpenCV
- Mediapipe
- pycaw

### Prerequisites

Install the following python packages to your env/vevn using the shell/bash.
* pip
  ```sh
  pip install opencv-python
  pip install mediapipe
  pip install pycaw
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SamirGouda/Gesture_Volume_Control_Project.git
   ```
   
2. Run the python file using from your terminal
   ```shell
   python gesture_volume_control.py
   ```



<!-- USAGE EXAMPLES -->
## Usage

- control the volume using your thumb and index fingers
- close the frame window by pressing the `q` button on your keyboard

[![fingers far from each other][screenshot-2]]

<!-- CONTACT -->
## Contact

Samir Gouda - [https://www.linkedin.com/in/samirgouda](https://www.linkedin.com/in/samirgouda) 

email: [samiir.ahmedd@gmail.com](mailto:samiir.ahmedd@gmail.com)

Project Link: [https://github.com/SamirGouda/Gesture_Volume_Control_Project](https://github.com/SamirGouda/Gesture_Volume_Control_Project)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew](https://github.com/othneildrew/) for his README template
* [murtazahassan](https://github.com/murtazahassan) for his computer vision course  




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/samirgouda/
[product-screenshot]: images/1.png
[screenshot-2]: images/2.png
[screenshot-3]: images/3.png