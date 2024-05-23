<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useArticleStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const store = useArticleStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()
const route = useRoute()  // 현재 라우트 인스턴스에 접근하기 위한 useRoute

const updateArticle = function () {
  const articleId = route.params.id;  // 수정

  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/articles/${articleId}/`,
    data: {
      title: title.value,
      content: content.value
    },
  })
    .then((response) => {
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>


<style>

</style>
