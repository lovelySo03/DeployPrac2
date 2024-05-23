import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter, useRoute } from "vue-router";

export const useUserStore = defineStore("user", () => {
  const user = ref(null);
  const subscribedSavings = ref([]);
  const subscribedDeposits = ref([]);
  const API_URL = "http://localhost:8000";
  const token = ref(localStorage.getItem("token") || null);
  const router = useRouter();
  const route = useRoute();
  const isLogin = computed(() => token.value !== null);

  const fetchUserProfile = async () => {
    try {
      
      const response = await axios.get(`${API_URL}/accounts/profile/`, {
        
        headers: {
          
          Authorization: `Token ${token.value}`,
        },
      });
      user.value = response.data;
    } catch (error) {
      console.error("UserProfile fetching error:", error);
    }
  };

  const deleteUser = async () => {
    try {
      await axios.delete(`${API_URL}/accounts/delete_user/`, {
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
      user.value = null;
    } catch (error) {
      console.error("Error deleting user:", error);
    }
  };

  const fetchUserInfo = async () => {
    try {
      const response = await axios.get(`${API_URL}/accounts/info/`, {
        headers: {
          Authorization: `Token ${token.value}`,
        },
      });
      subscribedSavings.value = response.data.subscribed_savings;
      subscribedDeposits.value = response.data.subscribed_deposits;
    } catch (error) {
      console.error("Error fetching user info:", error);
    }
  };

  const updateUser = async () => {
    try {
      const response = await axios.put(`${API_URL}/accounts/profile/`, user.value, {
        headers: {
          'Authorization': `Token ${token.value}`,
        },
      });
      // 요청 성공 후 응답 데이터를 처리
      console.log('업데이트 성공:', response.data);
    } catch (error) {
      // 에러 처리
      console.error('업데이트 에러:', error.response);
    }
  };
  

  const logIn = async (payload) => {
    try {
      const { username, password } = payload;
      const response = await axios.post(`${API_URL}/accounts/login/`, { username, password });
      token.value = response.data.key;
      localStorage.setItem("token", response.data.key);
      await fetchUserProfile(); // 로그인 후 사용자 프로필 가져오기
      router.push({ name: "Home" });
      
    } catch (error) {
      console.log(error);
    }
  };

  const logOut = () => {
    token.value = null;
    localStorage.removeItem("token");
    user.value = null;
    router.push({ name: "Home" });
  };

  const signUp = async (payload) => {
    try {
      const { username, password1, password2, email, nickname, age, money, salary } = payload;
      await axios.post(`${API_URL}/accounts/signup/`, { 
        username, 
        password1, 
        password2, 
        email,
        nickname,
        age,
        money,
        salary
      });
      console.log("회원가입 성공!");
      await logIn({ username, password: password1 });
      router.push({ name: "Home" });
    } catch (error) {
      if (error.response) {
        console.log("서버 응답 오류:", error.response.data); // 서버에서 반환하는 에러 메시지 출력
      } else if (error.request) {
        console.log("요청이 서버에 도달하지 못했습니다:", error.request); // 요청이 서버에 도달하지 못한 경우
      } else {
        console.log("설정 오류:", error.message); // 기타 설정 오류
      }
    }
  };
  
  return {
    user,
    subscribedSavings,
    subscribedDeposits,
    token,
    isLogin,
    fetchUserProfile,
    deleteUser,
    fetchUserInfo,
    updateUser,
    signUp,
    logIn,
    logOut,
  };
});
