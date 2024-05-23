<template>
  <h1>DetailView</h1>
  <div class="modal-btn">
    <!-- 수정 페이지로 이동 버튼 -->
    <button @click="goToEditPage">수정</button>
    <!-- 삭제 버튼 클릭 시 showModal을 true로 설정하여 모달을 보여줌 -->
    <button @click="showModal = true">삭제</button>
  </div>
  <div v-if="showModal" class="modal-wrap">
    <div class="modal-container">
      <h2>정말로 삭제하시겠습니까?</h2>
      <button @click="deleteArticle">예</button>
      <button @click="showModal = false">아니오</button>
    </div>
  </div>
  <!-- 게시글 조회 -->
  <div v-if="article">
    <p>게시글 번호 : {{ article.id }}</p>
    <p>게시글 제목 : {{ article.title }}</p>
    <p>게시글 내용 : {{ article.content }}</p>
    
    <p>작성 시간 : {{ article.created_at }}</p>
    <p>수정 시간 : {{ article.updated_at }}</p>
    <!-- 유저정보 -->
    <h3>작성자</h3>
    <p>작성자 아이디: {{ article.user.username }}</p>
    <p>작성자 이름 : {{ article.user.name }}</p>
    <p>작성자 닉네임 : {{ article.user.nickname }}</p>
    <!-- 게시글의 댓글 조회 및 수정,삭제 -->
    <div v-if="comments">
  <h2>Comments</h2>
  <ul>
    <li v-for="comment in comments" :key="comment.id">
      <div v-if="!comment.isEditing">
        <h4>작성자 : {{ comment.user.username }} <span v-if="comment.created_at !== comment.updated_at">(수정됨)</span></h4>
        <p>댓글 내용 : {{ comment.content }}</p>
        <p>댓글 작성 시간 : {{ comment.created_at }}</p>
        <!-- <p>댓글 수정 시간 : {{ comment.updated_at }}</p> -->
        <div class="modal-btn">
          <button @click="editComment(comment)">수정</button>
          <button @click="comment.showModal2 = true">삭제</button> <!-- 수정됨 -->
        </div>
        <div v-if="comment.showModal2" class="modal-wrap"> <!-- 수정됨 -->
          <div class="modal-container">
            <h2>정말로 댓글을 삭제하겠습니까?</h2>
            <button @click="deleteComment(comment)">예</button> <!-- 수정됨 -->
            <button @click="comment.showModal2 = false">아니오</button> <!-- 수정됨 -->
          </div>
        </div>
      </div>
      <div v-else>
        <textarea v-model="comment.editedContent"></textarea>
        <button @click="updateComment(comment)">저장</button>
        <button @click="cancelEdit(comment)">취소</button>
      </div>
    </li>
  </ul>
</div>
    <!-- 댓글 작성 란 -->
    <h2>댓글 작성</h2>
    <form @submit.prevent="createComment">
      <div>
        <label for="commentContent">댓글 내용: </label>
        <!-- 엔터로 댓글입력 되게 -->
        <!-- <textarea
            id="commentContent"
            v-model.trim="commentContent"
            @keydown.enter.prevent="
              ($event) => ($event.shiftKey ? null : createComment())
            "
          ></textarea> -->

        <!-- 그냥 엔터 시 줄바꿈 -->
        <textarea id="commentContent" v-model.trim="commentContent"></textarea>
      </div>
      <input type="submit" value="작성" />
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useArticleStore } from "@/stores/counter";
import { useRoute } from "vue-router";

const showModal = ref(false);
const showModal2 = ref(false);
const store = useArticleStore();
const route = useRoute();
const article = ref(null);
const comments = ref(null);
const commentContent = ref("");

import { useRouter } from "vue-router";
const router = useRouter();

//  댓글 조회
const getComments = function (articleId) {
  axios({
    method: "get",
    url: `${store.API_URL}/api/v1/articles/${articleId}/comments/`,
  })
    .then((res) => {
      comments.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
};

onMounted(() => {
  const articleId = route.params.id;

  axios({
    method: "get",
    url: `${store.API_URL}/api/v1/articles/${articleId}/`,
  })
    .then((res) => {
      article.value = res.data;
      article.value.content = res.data.content.replaceAll("\n", "<br />");
    })
    .catch((err) => {
      console.log(err);
    });

  getComments(articleId);
});

// 댓글작성
const createComment = function () {
  const articleId = route.params.id;
  if (!commentContent.value.trim()) {
    alert("댓글 내용을 입력해주세요.");
    return;
  }
  axios({
    method: "post",
    url: `${store.API_URL}/api/v1/articles/${articleId}/comments/`,
    data: {
      content: commentContent.value,
    },
      headers: {
        Authorization: `Token ${store.token}`
      }
  })
    .then((response) => {
      console.log(response.data)
      commentContent.value = "";
      getComments(articleId);
    })
    .catch((error) => {
      console.log(error);
    });
};

// 게시글 삭제
const deleteArticle = function () {
  const articleId = route.params.id;

  axios({
    method: "delete",
    url: `${store.API_URL}/api/v1/articles/${articleId}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(() => {
      alert("게시글이 삭제되었습니다.");
      router.push({ name: "ArticleView" }); // 혹은 사용자가 확인할 수 있는 다른 UI 피드백 제공
    })
    .catch((err) => {
      console.error(err);
    });
};

// 게시글 수정 페이지 이동
const goToEditPage = function () {
  const articleId = route.params.id;
  router.push({ name: "ArticleEdit", params: { id: articleId } });
};
const editComment = function (comment) {
  comment.isEditing = true;
  comment.editedContent = comment.content;
};

// 댓글 수정
const updateComment = function (comment) {
  const articleId = route.params.id;
  axios({
    method: "put",
    url: `${store.API_URL}/api/v1/articles/${articleId}/comments/${comment.id}/`,
    data: {
      content: comment.editedContent,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      comment.content = comment.editedContent;
      comment.isEditing = false;
      getComments(articleId);
    })
    .catch((error) => {
      console.log(error);
    });
};
// 댓글 수정 취소
const cancelEdit = function (comment) {
  comment.isEditing = false;
};

//댓글 삭제
// deleteComment 함수 수정
const deleteComment = function (comment) { // comment 파라미터 추가
  const articleId = route.params.id;

  axios({
      method: "delete",
      url: `${store.API_URL}/api/v1/articles/${articleId}/comments/${comment.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then(() => {
      alert("댓글이 삭제되었습니다.");
      comment.showModal2 = false; // 모달 닫기
      this.comments = this.comments.filter(c => c.id !== comment.id); // UI에서 댓글 제거
    })
    .catch((err) => {
      console.error(err);
    });
};

</script>

<style>
/* dimmed */
.modal-wrap {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
}
/* modal or popup */
.modal-container {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 550px;
  background: #fff;
  border-radius: 10px;
  padding: 20px;
  box-sizing: border-box;
}
</style>
