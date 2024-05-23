<template>
  <div>
      <div>
        <h2>가입상품목록</h2>
        <h4>예금목록</h4>
        <div v-for="deposit in user.subscribed_deposits" :key="deposit.id">
          <ul>
            <li>{{deposit.kor_co_nm}} - {{ deposit.fin_prdt_nm }}</li>
          </ul>
        </div>
        <h4>적금목록</h4>
        <div v-for="saving in user.subscribed_savings" :key="saving.id">
          <ul>
            <li>{{saving.kor_co_nm}} - {{ saving.fin_prdt_nm }}</li>
          </ul>
        </div>
      </div>

    </div>
</template>

<script>
import { useUserStore } from "@/stores/users";
import { onMounted, ref, reactive } from "vue";

export default {
  setup() {
    const userStore = useUserStore();
    const user = ref(null);

    const fetchUser = async () => {
      await userStore.fetchUserProfile();
      user.value = userStore.user;
      console.log(user.value)
    };


    onMounted(fetchUser);

    return {
      user,
      deleteUser: userStore.deleteUser,
    };
  },
};
</script>
