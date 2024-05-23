<!-- <template>
  <div v-if="product">
    <h2>{{ product.name }} 상세 정보</h2>
    <p>가입 기간: {{ product.joinPeriod }}</p>
    <p>금리: {{ product.interestRate }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue';
const props = defineProps({
  selectedProduct: Object })
const product = computed(() => {
  return props.selectedProduct;
});
</script> -->
<template>
  <div v-if="selectedProduct" class="product-modal">
    <button class="close-button" @click="closeModal">닫기</button>
    <h2>{{ selectedProduct.fin_prdt_nm }} 상세 정보</h2>
    <div class="modal-content">
      <p><strong>금융회사 명:</strong> {{ selectedProduct.kor_co_nm }}</p>
      <p><strong>가입 방법:</strong> {{ selectedProduct.join_way }}</p>
      <p><strong>만기 후 이자율:</strong> {{ selectedProduct.mtrt_int }}</p>
      <p><strong>우대조건:</strong> {{ selectedProduct.spcl_cnd }}</p>
      <p><strong>가입제한:</strong> {{ selectedProduct.join_deny }}</p>
      <p><strong>가입대상:</strong> {{ selectedProduct.join_member }}</p>
      <p><strong>기타 유의사항:</strong> {{ selectedProduct.etc_note }}</p>
      <p><strong>최고한도:</strong> {{ selectedProduct.max_limit }}</p>
      <p><strong>공시 시작일:</strong> {{ selectedProduct.dcls_strt_day }}</p>
      <p><strong>공시 종료일:</strong> {{ selectedProduct.dcls_end_day }}</p>
      <p><strong>금융회사 제출일:</strong> {{ selectedProduct.fin_co_subm_day }}</p>

      <div v-for="(option, index) in selectedProduct.options" :key="index">
        <p><strong>저축 금리 유형:</strong> {{ option.intr_rate_type_nm }}</p>
        <p><strong>저축 기간:</strong> {{ option.save_trm }}개월</p>
        <p><strong>저축 금리:</strong> {{ option.intr_rate }}%</p>
        <p><strong>최고 우대금리:</strong> {{ option.intr_rate2 }}%</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, watch, ref } from 'vue';

const props = defineProps({
  selectedProduct: Object
});

const selectedProduct = ref(props.selectedProduct);

const closeModal = () => {
  selectedProduct.value = null;
};

watch(() => props.selectedProduct, (newValue) => {
  selectedProduct.value = newValue;
});
</script>

<style scoped>
.product-modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 9999;
  max-width: 90%;
  max-height: 90%;
  overflow-y: auto;
}

.modal-content {
  max-height: 80vh;
  overflow-y: auto;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
}
</style>
