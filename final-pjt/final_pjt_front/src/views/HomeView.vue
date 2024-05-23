<template>
  <div class="totalbody">
    <div class="bodycontent0">
      <br>
    </div>

    <div class="caro-item-text">

      <div class="bodycontent1">
        <v-carousel
          cycle="false"
          hide-delimiters
          height="600"
          style="overflow: hidden;"
          :show-arrows="false"
          :autoplay="false"
        >
          <v-carousel-item>
            <div class="caro-item-text">
              <div class="title">
                <br>
                <br>
                <p>&nbsp;&nbsp;<span class="pink-text">금융의 모든 것</span></p>
                <p><span class="color">&nbsp;&nbsp;<span class="pink-text">머니멘토</span></span>에서 쉽고 간편하게</p>
              </div>
              &nbsp;&nbsp;
                <a 
                  href="#postList" 
                  class="btn btn-block custom-btn zindex">
                  금융상품 자유 게시판 바로가기
                </a>
            </div>
          </v-carousel-item>
        </v-carousel>
      </div>
      <br>
      <img src="@/assets/back2.jpg" alt="back1 이미지" class="back1-image">
      </div>
    <div class="bodycontent2">
      <br>
      <br>
      <br>
      <br>
    </div>
    <div class="move_container1_parent">
            <div class="move_container1" ref="container1">
              <!-- <img class="my-image1" src="@/assets/dog1.jpg" alt="그림"> -->
              <div class="my-element1">
                <h2>내 모든 금융 내역을 한눈에 조회하고 관리하세요.</h2>
                <h2>이제껏 경험 못 했던 쉽고 편리한 금융 서비스,</h2>
                <h2><span class="pink-text2">머니멘토</span>를 통해 당신의 일상이 새로워질 거예요.</h2>

              </div>
            </div>
          </div>
    <div class="bodycontent5">
      <div>
        <div>
          <!--  -->
          <div class="first">
            <div>
              <div class="container2">
                <br>
                <!-- <h2>만나서 반가워요</h2> -->
                <br>
              </div>
              <div class="move_container2" ref="container2">
                <img class="my-image2" src="@/assets/phone1.jpg" alt="그림">
                <div class="my-element2">
                  <br>
                  <br>
                  <h2>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;계좌와 카드를 연결해 보세요.</h2>
                  <h2>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;잔액 조회와 확인은 기본,</h2>
                  <h2>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;여러분의 시간을 아껴드릴게요</h2>
                </div>
              </div>
            </div>
            <div>
              <div>
                <div class="container4">
                  <h3 style="color: rgb(39, 44, 47); font-weight: bold; font-size: 30px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;홈 · 소비</h3>
                  <br>
                  <h1>&nbsp;&nbsp;&nbsp;내 돈 관리,</h1>
                  <h1>&nbsp;&nbsp;&nbsp;지출부터 일정까지</h1>
                  <h1>&nbsp;&nbsp;&nbsp;똑똑하게</h1>
                  <br>
                </div>
                <div class="move_container4" ref="container4">
                  <img class="my-image4" src="@/assets/phone2.jpg" alt="그림">
                  <div class="my-element4">
                    <br>
                    <br>
                    <br>
                    <br>
                    <!-- 스크롤할 때 애니메이션과 함께 나타남 4 -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="bodycontent6">
      <div class="container3">
        <br>
        <br>
        <!-- <h1>반가워요</h1> -->
      </div>
      <div class="move_container3" ref="container3">
        <!-- <img class="my-image3" src="@/assets/money.png" alt="그림"> -->
        <div class="my-element3">
          <!-- <h1>&nbsp;&nbsp;각 나라의 <span class="pink-text3" style="font-weight: bold;">환율</span>도 비교해보세요</h1> -->
        </div>
      </div>
    </div>
    <div class="bodycontent7">
      <img src="@/assets/people.jpg" alt="그림">
    </div>
    <div class="bodycontent8">
      <!-- <div class="container5" style="font-size: 50px;">
        <br>
        <br>
        <h1><span class="pink-text" style="font-weight: bold; font-size: 60px;">머니멘토</span>로</h1>
        <h1>나에게 딱 맞게</h1>
        <br>
        <br>
      </div> -->
      <br>
      <br>
      <div class="move_container5" ref="container5">
        <!-- <img class="my-image5" src="@/assets/money2.jpg" alt="그림"> -->
        <div class="my-element5">
          <div class="container5" style="font-size: 50px;">
        <br>
        <br>
        <h1><span class="pink-text" style="font-weight: bold; font-size: 60px;">머니멘토</span>로</h1>
        <h1>나에게 딱 맞게</h1>
      </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useUserStore } from '@/stores/users';



const userStore = useUserStore();

const container1 = ref(null);
const container2 = ref(null);
const container3 = ref(null);
const container4 = ref(null);
const container5 = ref(null);

const options = {
  root: null,
  rootMargin: '0px',
  threshold: 0.5
};

const createObserver = (elementClass, imageClass, container) => {
  return new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const elements = container.value.querySelectorAll(elementClass);
      const images = container.value.querySelectorAll(imageClass);
      if (entry.isIntersecting) {
        elements.forEach(element => {
          element.classList.add('show');
        });
        images.forEach(image => {
          image.classList.add('show');
        });
      } else {
        elements.forEach(element => {
          element.classList.remove('show');
        });
        images.forEach(image => {
          image.classList.remove('show');
        });
      }
    });
  }, options);
};

onMounted(() => {
  
  const observer1 = createObserver('.my-element1', '.my-image1', container1);
  observer1.observe(container1.value);

  const observer2 = createObserver('.my-element2', '.my-image2', container2);
  observer2.observe(container2.value);

  const observer3 = createObserver('.my-element3', '.my-image3', container3);
  observer3.observe(container3.value);

  const bodycontent1 = document.querySelector('.bodycontent1');
  setTimeout(() => {
    bodycontent1.classList.add('show');
  }, 900);

  const observer4 = createObserver('.my-element4', '.my-image4', container4);
  observer4.observe(container4.value);

  const observer5 = createObserver('.my-element5', '.my-image5', container5);
  observer5.observe(container5.value);

});
</script>

<style scoped>
.totalbody{
  /* margin-left: 12%;
  margin-right: 12%; */
  background-color:white;
}



.first {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    align-items: center;
    gap: 5px;
    height: 80vh;
}

.first > div {
    flex: 1; 
    margin: 0 5px; 
}

.bodycontent0 {
  height: 10vh; 
}
.bodycontent8 {
  height: 30vh;
}

.pink-text {
  color:  #e91e63; 
}

.pink-text3 {
  /* color:  rgb(39, 44, 47); */
  /* color: rgb(77, 67, 153); */
  color: rgb(247,233,186);
}
.pink-text2 {
color: #e91e63; 
}

.bodycontent1 {
  height: 100vh;
  display: flex;
  justify-content: center; 
  align-items: center;
}

.changemoeny {
  display: flex; 
}

.totalbody {
  display: flex;
  flex-direction: column; 
  /* margin-left: 12%;
  margin-right: 12%; */
}
.my-element1 h2 {
  margin: 20px 0;
  font-weight: 800;
  color: black;
}

.container5 h2 {
  margin: 10px 0; 
  font-weight: 800;
}

.back1-image {
  width: 100%; 
  height: auto; 
}

@media screen and (min-width: 768px) {
  .totalbody {
    flex-direction: column; 
    margin-left: 12%;
    margin-right: 12%;
  }
}

.v-carousel {
  border-bottom: 1px solid #DBDBDB;
}
.bodycontent2{
  background-color: rgb(249, 250, 252);
}
.title {
  margin: 5px 0;
  font-size: 40px;
  font-weight: 900;
  letter-spacing: -2px;
}

.caro-item-img {
  position: absolute;
  right: 17vw;
}

@media (max-width: 1250px) {
  .caro-item-img {
    right: 10vw;
  }
}

@media (min-width: 1600px) {
  .caro-item-img {
    right: 20vw;
  }

  .caro-item-text {
    left: 20vw;
  }
}

.container {
  width: 1400px;
  margin-top: 2rem auto;
  margin-bottom: 2rem auto;
}

.custom-btn {
  background-color:#e91e63; 
  color: white; 
  border-radius: 1.5rem;
  font-size: 1.5rem; 
  transition: background-color 0.3s ease;
}

.custom-btn:hover {
  background-color: rgb(77, 67, 153);
}

.pink-btn {
  background-color: rgb(39, 44, 47);
}

.navbar {
  transition: height 0.3s ease;
}

.my-element1, .my-element3,.my-element4,.my-element5,
.my-image1, .my-image2, .my-image3, .my-image4, .my-image5 {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.7s ease-out, transform 0.7s ease-out;
}

.my-element1.show, .my-element2.show, .my-element3.show, .my-element4.show, .my-element5.show,
.my-image1.show, .my-image2.show, .my-image3.show, .my-image4.show, .my-image5.show {
  opacity: 1;
  transform: translateY(0);
}
.move_container2 {
  height: 1vh;
}

.my-element2 {
  margin-left: 40px; 
}

.move_container3 {
  height: 30vh;
}

.move_container5 {
  height: 10vh;
}

.move_container4 {
  height: 5vh;
  margin-top: 10vh;
}

.container1 {
  height: 20vh;
}

.container4 {
  height: 60vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-end; 
  font-weight: 800; 
}

.container2 {
  height: 1vh;
}

.container3 {
  height: 70vh;
}

.container5 {
  height: 60vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* padding-left: 50px; */
  font-weight: 800;  
}

.my-element5 h1 {
  font-weight: 800;
}

.move_container1 {
  margin-top: 10vh;
  text-align: center;
  height: 40vh; 
  /* margin-left: 10%;
  margin-right: 10%; */
  font-weight: 800;
  
 
}
.move_container1_parent {
  position: relative;
  width: 100%;
  background-color: rgb(249, 250, 252);

}

.move_container1_parent::before {
  content: ""; 
  position: absolute; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 100%; 
  background-color: rgb(249, 250, 252);
  z-index: -1; 
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.bodycontent1 {
  height: 30vh;
  opacity: 0; 
  transition: opacity 1s ease;
}

.bodycontent1.show {
  opacity: 1; 
  
}

.back1-image {
    z-index: -1000;
}

.zindex {
  z-index: 1000;
}
</style>


