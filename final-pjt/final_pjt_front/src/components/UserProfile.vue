<template>
  <div class="container">
    <!-- <h1>회원정보관리 페이지</h1> -->
    <div class="user-info" v-if="user">
      <br>
      <hr>
      <div class="middle2">
        <h2>프로필 정보</h2>
      </div>
      <hr>
      <br>
      <div class="middle1">

        <div class="profile">
          <br>
          <table>
            <tr>
              
              <div class="middle4">
              <!-- <img :src="user.user_data.profile_img" alt="@/assets/profile.png" /> -->
              <img v-if="user.user_data.profile_img" :src="user.user_data.profile_img" alt="프로필 이미지" />
              <img v-else src="@/assets/profile.png" alt="프로필 이미지" />
              <br>
               </div>
            
            </tr>
    
            <tr><br>
              
              <h5 style="text-align: center;">&nbsp;&nbsp;&nbsp;반갑습니다, {{ user.user_data.nickname ? user.user_data.nickname : '회원' }}님</h5>

            
            </tr>
          </table>
        
      </div>
      <div class="details">
        <table>
          <tr>
            <td><label>회원번호</label></td>
            <td>{{ user.user_data.pk }}</td>
          </tr>
          <tr>
            <td><label>ID</label></td>
            <td>{{ user.user_data.username }}</td>
          </tr>
          <tr>
            <td><label>이메일</label></td>
            <td>{{ user.user_data.email }}</td>
          </tr>
          <tr>
            <td><label>닉네임</label></td>
            <td>{{ user.user_data.nickname }}</td>
          </tr>
          <tr>
            <td><label>이름</label></td>
            <td>{{ user.user_data.first_name }} {{ user.user_data.last_name }}</td>
          </tr>
          <tr>
            <td><label>나이</label></td>
            <td>{{ user.user_data.age }}</td>
          </tr>
          <tr>
            <td><label>자산</label></td>
            <td>{{ user.user_data.money }}</td>
          </tr>
          <tr>
            <td><label>연봉</label></td>
            <td>{{ user.user_data.salary }}</td>
          </tr>
        </table>
      </div>

      </div>

      <br>
      <br>
      <hr>




      <div class="products">
        <h2>가입상품 목록</h2>

        <table class="table-container">
          <tr>
            <td>예금 목록</td>
            <td>적금 목록</td>
          </tr>

          <tr>
            <td>
              <!-- 예금 -->
              <ul>
            <li v-for="deposit in user.subscribed_deposits" :key="deposit.id">{{ deposit.kor_co_nm }} - {{ deposit.fin_prdt_nm }}</li>
              </ul>
            </td>
            <td>
              <!-- 적금 -->
              <ul>
            <li v-for="saving in user.subscribed_savings" :key="saving.id">{{ saving.kor_co_nm }} - {{ saving.fin_prdt_nm }}</li>
              </ul>
            </td>
          </tr>
        </table>
    

      </div>




      <br>
      <div class="final">

        <div class="out">
        <button onclick="window.location.href = 'https://bayleaf07.pe.kr/cat/'">⭐마이펫🐕⭐</button>
      </div>

      <div class="out">
        <button @click="deleteUser">회원 탈퇴</button>
      </div>

      </div>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/users";
import { onMounted, ref } from "vue";

export default {
  setup() {
    const userStore = useUserStore();
    const user = ref(null);

    const fetchUser = async () => {
      await userStore.fetchUserProfile();
      user.value = userStore.user;
      console.log(user.value);
    };

    const deleteUser = async () => {
      try {
        await userStore.deleteUser();
        window.alert('탈퇴 되었습니다.');
        router.push("home");
      } catch(error) {
        console.error("Error deleting user:", error);
      }
    };

    onMounted(fetchUser);

    return {
      user,
      deleteUser,
    };
  },
};
</script>
<style scoped>
/* .middle2 {
  background-color: #adb5bd;
} */

.middle1 {
  display: flex;
}

.middle1 .profile {
  flex: 1; 
}

.middle1 .details {
  flex: 2; 
}

.middle1 .details table {
  width: 100%;
}

.middle1 .details table td {
  padding: 10px;
  font-size: 16px;
  text-align: center;
}

.out {
  text-align: right;
  margin-right:3%;
}

.out button {
  border: 1px solid #ccc; 
  border-radius: 5px; 
  /* padding: 10px 20px;  */
  font-size: 16px; 
  cursor: pointer; 
  background-color: transparent; 
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.user-info {
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
}

.profile img {
  max-width: 150px;
  border-radius: 50%;
}

.details table {
  width: 100%;
  margin-top: 20px;
  table-layout: fixed;
}

.details td {
  padding: 10px;
  font-size: 16px;
  text-align: center;
  width: 50%; 
}

.products {
  margin-top: 20px;
  text-align: center;
}

.products h4 {
  margin-bottom: 10px;
}

.details table {
  width: 100%;
  border-collapse: collapse; 
  border-radius: 5px; 
}

.details table td, .products table td, .products table th,
.details table th {
  border: 1px solid #ccc;
  padding: 10px;
  font-size: 16px;
  text-align: center;
  border-radius: 5px; 
}

.table-container {
  width: 100%;
}

.table-container table {
  width: 100%; 
  border-collapse: collapse;
}

.table-container td, 
.table-container th {
  border: 1px solid #ccc;
  padding: 10px;
  font-size: 16px;
  text-align: center;
  width: 50%; 
  border-radius: 5px; 
}

.final {
    display: flex;
    gap: 2px;
    justify-content: flex-end; 
  }
.middle4 {
  margin-left: 20%;
  text-align: center;
}
</style>