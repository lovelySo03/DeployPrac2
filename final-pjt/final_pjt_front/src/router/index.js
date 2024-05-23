import { createRouter, createWebHistory } from "vue-router";
import ArticleView from "@/views/ArticleView.vue";
import DetailView from "@/views/DetailView.vue";
import CreateView from "@/views/CreateView.vue";
import ArticleEditView from "@/views/ArticleEditView.vue";
// import KakaoMap from "@/components/KakaoMap.vue";
import UserProfile from '@/components/UserProfile.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import HomeView from '@/views/HomeView.vue'
import UpdateView from '@/views/UpdateView.vue'
import SubscribeView from '@/views/SubscribeView.vue'
// NKJ
import FxView from '@/views/NKJ/FxView.vue'
import KakaoMap from '@/views/NKJ/KakaoMap.vue'
import ProductView from '@/views/NKJ/ProductView.vue'
// SY
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/'
      ,name:'Home',
      component:HomeView
    },
    {
      path: "/article",
      name: "ArticleView",
      component: ArticleView,
    },
    {
      path: "/articles/:id",
      name: "DetailView",
      component: DetailView,
    },
    {
      path: "/create",
      name: "CreateView",
      component: CreateView,
    },
    {
      path: "/article/edit/:id",
      name: "ArticleEdit",
      component: ArticleEditView,
    },
    // NKJ
    {
      path: "/Map",
      name: "KakaoMap",
      component: KakaoMap,
    },
    {
      path:"/Fx",
      name: "Fx",
      component: FxView,
    },
    {
      path:"/Map",
      name: "Map",
      component: KakaoMap,
    },
    {
      path:"/Product",
      name:"Product",
      component:ProductView
    },
    // SY
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/login",
      name: "LogInView",
      component: LogInView,
    },
    {
      path:'/profile',
      name:'profile',
      component:UserProfile,
      children:[
        {
          path:'/updateuser',
          name:'updateUser',
          component:UpdateView
        },
        {
          path:'/subscribe',
          name:'subscribe',
          component:SubscribeView
        }

      ]
    },
  ],
});

import { useArticleStore } from "@/stores/counter";
import { useUserStore } from "@/stores/users";


router.beforeEach((to, from) => {
  const store = useUserStore()
  
  // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
  if ( (to.name === 'profile' || to.name==='CreateView') && (store.isLogin === false)) {
    window.alert('로그인이 필요해요!!')
    return { name: 'LogInView' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'Home' }
  }

})

export default router;
