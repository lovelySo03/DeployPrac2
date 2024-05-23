<template>
  <div class="container1">
    <br>
  </div>
  <div class="container">
    <h1 class="title">Sign Up</h1>
    <form @submit.prevent="signUp" class="form">
      <div class="input-group">
        <!-- <label for="username">ID : </label> -->
        <input type="text" v-model.trim="username" id="username" placeholder="Enter your ID">
      </div>
      <div class="input-group">
        <!-- <label for="password1">비밀번호 : </label> -->
        <input type="password" v-model.trim="password1" id="password1" placeholder="Enter your password">
      </div>
      <div class="input-group">
        <!-- <label for="password2">비밀번호 확인 : </label> -->
        <input type="password" v-model.trim="password2" id="password2" placeholder="Confirm your password">
      </div>
      <div class="input-group">
        <!-- <label for="email">이메일 : </label> -->
        <input type="email" v-model="email" id="email" placeholder="Enter your email">
      </div>
      <div class="input-group">
        <!-- <label for="nickname">닉네임 : </label> -->
        <input type="text" v-model.trim="nickname" id="nickname" placeholder="Enter your nickname">
      </div>
      <div class="input-group">
        <!-- <label for="age">나이 : </label> -->
        <input type="number" v-model.trim="age" id="age" placeholder="Enter your age">
      </div>
      <div class="input-group">
        <!-- <label for="money">자산 : </label> -->
        <input type="number" v-model="money" id="money" placeholder="Enter your asset amount">
      </div>
      <div class="input-group">
        <!-- <label for="salary">연봉 : </label> -->
        <input type="number" v-model="salary" id="salary" placeholder="Enter your salary">
      </div>
      <input type="submit" class="btn-submit" value="Submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'

const username = ref('') 
const password1 = ref('')
const password2 = ref('')
const nickname = ref('')
const age = ref(null)
const money = ref(null)
const salary = ref(null)
const email = ref('')

const store = useUserStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    email: email.value
  }
  store.signUp(payload)
}
</script>

<style scoped>
.container1{
  height: 10vh;
}

.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
  background-color: white;
}

.title {
  margin-bottom: 20px;
  font-size: 24px;
  color: black;
  text-align: center;
}

.form {
  text-align: center;
}

.input-group {
  margin-bottom: 15px;
  text-align: center;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  text-align: center;
}

input[type="text"],
input[type="password"],
input[type="email"],
input[type="number"] {
  width: calc(100% - 20px);
  padding: 10px;
  border: none;
  border-bottom: 2px solid black;
  border-radius: 0;
  outline: none;
  background-color: transparent;
}

input[type="submit"].btn-submit {
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
  margin-top: 20px;
}

input[type="submit"].btn-submit:hover {
  background-color:  #e91e63;
}
</style>
