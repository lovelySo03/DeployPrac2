<template>
  <div class="container0">
    <div class="container1">
      <br>
    </div>

    <div class="container">
      <div class="login-wrapper" v-if="!store.isLogin">
        <br>
        <h1 v-if="!isAuthenticated" class="title">Login&nbsp;&nbsp;&nbsp;</h1>
        <form v-if="!isAuthenticated" @submit.prevent="logIn">
          <div class="input-group">
            <!-- <label for="username">ID </label> -->
            <br>
            <input type="text" v-model.trim="username" id="username" placeholder="Enter your ID">
          </div>
          <div class="input-group">
            <!-- <label for="password">PW </label> -->
            <br>
            <input type="password" v-model.trim="password" id="password" placeholder="Enter your password">
          </div>
          <div>
            <input type="submit" class="btn-submit">
          </div>
        </form>
        <br>
        <div class="middle">
          <p>Forget Password?</p>
          <p>회원가입</p>
        </div>
        <br>
        <br>
      </div>

      <div class="welcome-wrapper" v-else>
        <h1>환영합니다</h1>
        <button @click="logOut" class="btn-logout">로그아웃</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useUserStore } from "@/stores/users";

const username = ref('');
const password = ref('');
const store = useUserStore();

// computed를 사용하여 반응형으로 상태를 관찰합니다.
const isAuthenticated = computed(() => store.isAuthenticated);
const user = computed(() => store.user);

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};

const logOut = () => {
  store.logOut();
};
</script>

<style scoped>

.middle {
  text-align: center;
  font-size: 13px; 
  margin-right: 20px;
}

.middle p {
  display: inline-block; 
  margin: 0 15px; 
  color: red; 
}

.container1 {
  height: 20vh;
}

.container0 {
  background-color: white;
}

h1.title {
  margin-bottom: 20px;
  font-size: 24px;
  color: black;
  text-align: center;
}

.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
  background-color: white;
}

.login-wrapper, .welcome-wrapper {
  text-align: center;
  border: none;
}

h1 {
  margin-bottom: 20px;
  font-size: 24px;
  color: #333;
}

.input-group {
  margin-bottom: 15px;
  text-align: center;
}

.middle{
  text-align: center;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  text-align: center;
}

input[type="text"],
input[type="password"] {
  width: calc(100% - 20px);
  padding: 10px;
  border: none;
  border-bottom: 2px solid black;
  border-radius: 0;
  outline: none;
  background-color: transparent;
}

input[type="submit"],
.btn-logout {
  width: 85%; 
  padding: 10px;
  border: none;
  border-radius: 20px;  
  color: #fff;
  background-color: #e91e63;
  cursor: pointer;
  font-size: 16px;
  margin: 0 auto;  
  display: block;  
  text-align: center;
  margin-left: 13px;
}

input[type="submit"]:hover,
.btn-logout:hover {
  background-color: #00b368;
}

.btn-logout {
  margin-top: 20px;
  background-color: #dc3545;
}

.btn-logout:hover {
  background-color: #c82333;
}

</style>
