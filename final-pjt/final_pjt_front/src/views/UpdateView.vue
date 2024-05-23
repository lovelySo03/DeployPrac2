<template>
  <div>
    <h2>회원정보</h2>
    <div v-if="user">
      <img :src="user.user_data.profile_img" alt="Profile Image" />
      
      <div>
        <label >회원번호:</label>
        {{ user.user_data.pk }}
      </div>
      <div>
        <label>ID:</label>
       {{user.user_data.username}}
      </div>

      <div>
        <label>이메일:</label>
        {{ user.user_data.email }}
      </div>

      <div>
        <label>닉네임:</label>
        <p v-if="!editModes.nickname">{{ user.user_data.nickname }}</p>
        <input v-else v-model="editableUser.nickname" />
        <button @click="toggleEdit('nickname')">{{ editModes.nickname ? 'Save' : 'Edit' }}</button>
      </div>

      <div>
        <label>이름:</label>
        {{ user.user_data.first_name }} {{ user.user_data.last_name }}
  
      </div>

      <div>
        <label>나이:</label>
        <p v-if="!editModes.age">{{ user.user_data.age }}</p>
        <input v-else v-model="editableUser.age" />
        <button @click="toggleEdit('age')">{{ editModes.age ? 'Save' : 'Edit' }}</button>
      </div>

      <div>
        <label>자산:</label>
        <p v-if="!editModes.money">{{ user.user_data.money }}</p>
        <input v-else v-model="editableUser.money" />
        <button @click="toggleEdit('money')">{{ editModes.money ? 'Save' : 'Edit' }}</button>
      </div>

      <div>
        <label>연봉:</label>
        <p v-if="!editModes.salary">{{ user.user_data.salary }}</p>
        <input v-else v-model="editableUser.salary" />
        <button @click="toggleEdit('salary')">{{ editModes.salary ? 'Save' : 'Edit' }}</button>
      </div>


      <button @click="deleteUser">회원 탈퇴</button>
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
    const editableUser = reactive({});
    const editModes = reactive({
      username: false,
      email: false,
      nickname: false,
      name: false,
      age: false,
      money: false,
      salary: false,
    });

    const fetchUser = async () => {
      await userStore.fetchUserProfile();
      user.value = userStore.user;
      console.log(user.value)
      Object.assign(editableUser, user.value.user_data);
    };

    const toggleEdit = (field) => {
      if (editModes[field]) {
        // Save the updated user data if the field is being saved
        userStore.updateUserProfile(editableUser);
      }
      editModes[field] = !editModes[field];
    };

    onMounted(fetchUser);

    return {
      user,
      editableUser,
      editModes,
      toggleEdit,
      deleteUser: userStore.deleteUser,
    };
  },
};
</script>
