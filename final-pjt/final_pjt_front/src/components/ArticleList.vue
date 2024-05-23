<template>

  <div class="container">
    <div class="header">
      <h2>금융상품 자유 게시판</h2>
      <div class="middle1">
        <RouterLink :to="{ name: 'CreateView' }">
          <button type="button" class="pink-button">글쓰기</button>
        </RouterLink>
      </div>
    <ArticleListItem 
      v-for="article in paginatedArticles"
      :key="article.id"
      :article="article"
    />
    </div>

    
    <div class="pagination">
      <button 
        v-for="page in totalPages" 
        :key="page" 
        @click="currentPage = page">
        {{ page }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { ref, computed } from 'vue'
import { useArticleStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useArticleStore()
const currentPage = ref(1)
const itemsPerPage = 10

const totalPages = computed(() => {
  return Math.ceil(store.articles.length / itemsPerPage)
})

const paginatedArticles = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return store.articles.slice(start, end)
})

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
.middle1 {
  text-align: right;
}

.header {
  text-align: center;
}

.pagination button {
  margin-right: 5px;
  padding: 5px 10px;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 3px;
  cursor: pointer;
  display: inline-block; 
}

.pagination button:hover {
  background-color: #eaeaea;
}

.pagination button.active {
  background-color:  rgb(255,78,124);
  color: white;
}

.header h2 {
  color: purple;
}
.no-underline {
  text-decoration: none;
}
.center {
  text-align: center;
}


.container {
  width: 800px;
  margin: 2rem auto;
}

.container > * {
  margin: 1rem;
}

.table, .table-header, .table-row {
  border: 1px solid #ccc;
  border-radius: 5px;
}

.table-header {
  display: flex;
  background-color: rgb(255,78,124);
  border-bottom: 1px solid #ccc;
}

.header-cell {
  padding: 10px;
}

.table-cell {
  padding: 10px;
  text-align: center;
}

.table-row, .pagination button {
  display: flex;
  align-items: center;
  transition: background-color 0.2s;
  cursor: pointer;
}

.table-row:hover {
  background-color: rgb(247, 250, 253);
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end; 
}

.pagination button {
  margin-right: 5px;
  padding: 5px 10px;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 3px;
  cursor: pointer;
  display: inline-block; 
}

.pagination button:hover {
  background-color: #eaeaea;
}

.pagination button.active {
  background-color:  rgb(255,78,124);
  color: white;
}

.table-cell {
  min-width: 0;
  overflow: hidden; 
  white-space: nowrap; 
  text-overflow: ellipsis;
}

.column-number {
  flex: 0.1;
}

.column-title {
  flex: 0.6;
}

.column-detail {
  flex: 0.3;
}

.pink-button {
  background-color: rgb(255,78,124);
  border: none;
  padding: 5px 9px;
  border-radius: 5px;
  color: white;
  cursor: pointer;
}

@media (max-width: 768px) {
  .container {
    width: 90%;
  }
  
  /* 반응형 */
  .pagination {
    margin-right: 5%; 
  }
}

@media (min-width: 769px) {
  .pagination {
    margin-right: 10%; 
  }
}
</style>
