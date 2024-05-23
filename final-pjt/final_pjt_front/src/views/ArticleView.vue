<template>
  <div>
    <!-- <h1>Article Page</h1> -->
    <!-- <RouterLink :to="{ name: 'CreateView' }">
      글쓰기
    </RouterLink> -->
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>
