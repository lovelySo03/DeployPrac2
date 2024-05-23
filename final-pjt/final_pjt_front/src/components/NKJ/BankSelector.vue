<template>
  <div class="total">
    <div class="first">
    <br>
  </div>
  <div class="middle1 d-flex justify-content-center">
    <select v-model="selectedBank" @change="fetchProducts">
      <option value="">전체 은행</option>
      <option v-for="bank in banks" :key="bank.id" :value="bank.name">{{ bank.name }}</option>
    </select>
    &nbsp;&nbsp;&nbsp;
    <label for="bank" class="label btn btn-primary" >은행 선택</label>
  </div>
  </div>
</template>

<script setup>
import { ref,watchEffect} from 'vue';

// 부모로부터 전달된 이벤트를 정의합니다.
const emits = defineEmits(['fetchProductsCallback']);

const selectedBank = ref(null);
const banks = [
  { id: 1, name: '국민은행' },
  { id: 2, name: '우리은행' },
  { id: 3, name: '대구은행' },
  { id: 4, name: '부산은행' },
  { id: 5, name: '광주은행' },
  { id: 6, name: '제주은행' },
  { id: 7, name: '전북은행' },
  { id: 8, name: '경남은행' },
  { id: 9, name: '중소기업은행' },
  { id: 10, name: '한국산업은행' },
  { id: 11, name: '신한은행' },
  { id: 12, name: '농협은행주식회사' },
  { id: 13, name: '하나은행' },
  { id: 14, name: '주식회사 케이뱅크' },
  { id: 15, name: '수협은행' },
  { id: 16, name: '주식회사 카카오뱅크' },
  { id: 17, name: '토스뱅크 주식회사' },
];

const fetchProducts = () => {
  // console.log(selectedBank.value)
  emits('fetchProductsCallback', selectedBank.value);
};
watchEffect(()=>{
  fetchProducts()
})
</script>

<style scoped>
.first{
  height: 5vh;
}

.total {
  margin-left: 10%;
}

.label {
  font-weight: bold;
  text-align: center;
  background-color: #FFD700; 
  color:black;
  border: 2px solid #ffffff; 
}

.label:hover {
  background-color: #FFD700; 
  border: 2px solid #ffffff; 
  color:black;
}
</style>
