<template>
  <div class="totalcontent">

    <nav class="navbar navbar-expand-lg">
    <RouterLink class="navbar-brand" :to="{ name: 'Home' }">
      <div class="title1">
      <img src="@/assets/logo.png" alt="logo" />
        Money Mentor
      </div>
    </RouterLink>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon">&nbsp;</span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <div class="middle">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item"></li>
        <li class="nav-item">
          <RouterLink class="nav-link compare-link" :to="{ name: 'Product' }">금리비교</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link compare-link" :to="{ name: 'Fx' }">환율계산</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link compare-link" :to="{ name: 'Map' }">주변은행</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link compare-link" :to="{ name: 'ArticleView' }">커뮤니티</RouterLink>
        </li>
      </ul>
      </div>
      <div class="navbar-nav ms-auto">
        <div class="second">
            <div v-if="!userStore.isLogin" class="d-flex">
              <button class="btn signup-link2 me-2" @click="goToLogin">로그인</button>
              <RouterLink class="nav-link signup-link" :to="{ name: 'SignUpView' }">회원가입</RouterLink>
            </div>
            <div v-if="userStore.isLogin" class="d-flex">
              <RouterLink class="nav-link" :to="{ name: 'profile' }">프로필</RouterLink>
              <button @click="logOut" class="nav-link btn">로그아웃</button>
            </div>
        </div>
      </div>
    </div>
  </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/users';
import { RouterLink, useRouter } from 'vue-router';

const userStore = useUserStore();
const router = useRouter();

const logOut = () => {
  userStore.logOut();
  router.push({ name: 'Home' });
};

const goToLogin = () => {
  router.push({ name: 'LogInView' });
};
</script>

<style scoped>

.title1 {
  font-weight: 700; 

  color: #e91e63;
 } 

.totalcontent { 
 background-color: white;
 color:black;
 margin-left: 10%;
 margin-right: 3%;
} 


.navbar-brand img {
  height: 30px;
  margin-right: 10px;
}

.navbar-toggler {
  border: none;
  /* background-color:rgb(255, 132, 133);*/
  margin-right: 15px;
}

.nav-link {
  cursor: pointer;
}


.signup-link {
  color: black;
  /* 
  background-color:rgb(255, 132, 133);
  border-color: rgb(39, 44, 47); */
  padding: 0.375rem 0.75rem;
  border-radius: 0.25rem;
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, color 0.15s ease-in-out;
}


.signup-link2 {
  color: black;
  /* background-color:rgb(255, 132, 133);
  border-color: rgb(255, 132, 133); */
  padding: 0.375rem 0.75rem;
  border-radius: 0.25rem;
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, color 0.15s ease-in-out;
}

 .signup-link:hover {
  color:  #D4B886;
  /* background-color: #D4B886; */
  /* border-color:  rgb(39, 44, 47); */
}

.signup-link2:hover {
  color: #D4B886;
  /* background-color: #D4B886; */
  /* border-color: black; */
}

.btn-primary {
  /* border-color: black; */
  color: black;
}

.btn-primary:hover {
  background-color: #D4B886;
  /* border-color: rgb(39, 44, 47); */
}
 
.compare-link {
  color:black;
}

.compare-link:hover {
  color:#D4B886;
} 

.navbar-toggler-icon {
  /* background-color: rgb(255, 132, 133); */
  border-radius: 25%;
  padding: 0.2rem 0.4rem;
}

.middle {
  display: flex;
  flex-wrap: nowrap;
}

.middle .nav-item {
  margin-right: 5px; 
}


@media (min-width: 768px) {
  .middle .nav-item {
    margin-right: calc(1rem + 2vw);
  }
}

@media (min-width: 1200px) {
  .middle .nav-item {
    margin-right: calc(1rem + 3vw);
  }
}

</style>
