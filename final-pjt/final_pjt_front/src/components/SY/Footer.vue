<script setup>

</script>

<template>
  <footer class="px-5 py-10">
    <div class="upper mx-3">
      <br>
      <RouterLink class="logo" :to="{ name: 'Home' }">
        <!-- <img src="@/assets/logo.png" alt="logo" /> -->
      Money Mentor
      </RouterLink>
      <hr>
      <br>
      <p class="font-weight-bold">(주) 머니멘토 컴퍼니</p>
      <p> 사업자 등록번호 : 123-45-67890 | 대표 : 김머니 </P>
      <p> 호스팅 서비스 : 주식회사 머니멘토 | 통신판매업 신고번호 : 1234-광주전남-01234 사업자정보확인 </P>
      <p> 12345 광주광역시 광산구 벚꽃산단 1번로 2층 </p>
      <p> 고객센터 : 광주광역시 광산구 벚꽃산단 1번로 (나무캠퍼스 빌딩) </P>
      <br>
    
    </div>
    <v-divider class="my-3"></v-divider>
    <div class="d-flex flex-row-reverse mx-3">
      <div>
        <p class="font-italic">Copyright ©Money Mentor All Rights Reserved.</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.container {
  width: 100vw;
}

footer {
  width: 100%;
  background-color:rgb(25,31,40) /* Light purple background */
}

.logo {
  display: flex;
  align-items: center;
  gap: 5px;
  color: white;
  font-size: 30px;
  text-decoration: none;
  font-family: 'Francois One', sans-serif;
  margin: 0 1rem;
}

.logo img {
  height: 36px;
}

.upper {
  color:white; /* Medium purple */
}

.v-divider {
  background-color: white;
}

footer p {
  color:white;
}

footer p.font-weight-bold {
  font-weight: bold;
}

footer p.font-italic {
  font-style: italic;
}
</style> 