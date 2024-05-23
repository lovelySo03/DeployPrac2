<template>
  <div class="container">
    <!-- <h5>게시글번호 : {{ article.id }}</h5>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성자 : {{ article.user.username }}</p> -->


    <div class="table">
      <div class="table-header">
        <div class="table-cell header-cell center column-number">번호</div>
        <div class="table-cell header-cell center column-title">제목</div>
        <div class="table-cell header-cell center column-detail">작성자</div>
        <!-- <div class="table-cell header-cell center column-writer">작성자</div> -->
      </div>
      <div class="table-row">
        <div class="table-cell center column-number">{{ article.id }}</div>
        <!-- <div class="table-cell center column-title">{{ article.title }}</div> -->
        <div class="table-cell center column-title">
          <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">{{ article.title }}</RouterLink>
        </div>
        <div class="table-cell center column-detail">{{ article.user.username }}</div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>


<style scoped>
.header h2 {
  color: purple;
}
.no-underline {
  text-decoration: none;
}
.center {
  text-align: center;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
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
  color: white;
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

/* 각 열의 너비 지정 */
.column-number {
  flex: 0.1;
}

.column-title {
  flex: 0.6;
}

.column-detail {
  flex: 0.3;
}


/* 모바일 화면에 대응하기 위한 media query */
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
