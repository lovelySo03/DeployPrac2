<template>
  <div class="container">
    <br>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle" class="form">
      <div class="form-group">
        <label for="title" class="label">제목</label>
        <input type="text" v-model.trim="title" id="title" class="input">
      </div>
      <div class="form-group">
        <label for="content" class="label">내용</label>
        <textarea v-model.trim="content" id="content" class="textarea" style="height: 300px;"></textarea>
      </div>
      <!-- <input type="submit"> -->
      <button type="submit" class="button">작성 완료</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useArticleStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useArticleStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()
console.log(store.token)
const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      console.log(response.data)
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Roboto', sans-serif; 
}
h1 {
  color: green;
}

.form {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
}

.label {
  font-weight: bold;
}

.input,
.textarea {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-left: auto; 
  margin-right: 15px; 
}

.button:hover {
  background-color: #45a049;
}
</style>
