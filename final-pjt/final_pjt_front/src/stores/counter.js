import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter, useRoute } from "vue-router";

export const useArticleStore = defineStore(
  "ArticleCounter",
  () => {
    const articles = ref([]);
    const API_URL = "http://127.0.0.1:8000";
    const token = ref(localStorage.getItem("token") || null); // 토큰을 localStorage에서 가져옴
    const router = useRouter();
    const route = useRoute(); // 현재 라우트에 대한 접근

    const isLogin = computed(() => token.value !== null);

    const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((response) => {
          articles.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const deleteArticle = function () {
      const articleId = route.params.id;

      axios({
        method: "delete",
        url: `${API_URL}/api/v1/articles/${articleId}/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then(() => {
          alert("게시글이 삭제되었습니다.");
          router.push({ name: "Home" });
        })
        .catch((err) => {
          console.error(err);
        });
    };

    const goToEditPage = function () {
      const articleId = route.params.id;
      router.push({ name: "ArticleEdit", params: { id: articleId } });
    };


    return {
      articles,
      API_URL,
      getArticles,
      deleteArticle,
      goToEditPage,
      token,
      isLogin,
    };
  },
  { persist: true }
);
