<template>
  <div>
    <BankSelector @fetchProductsCallback="fetchProducts" />
    <ProductList :products="products" />
    <ProductDetailModal :selectedProduct="selectedProduct" />
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';
import BankSelector from '@/components/NKJ/BankSelector.vue';
import ProductList from '@/components/NKJ/ProductList.vue';
import { fetchProductsFromDatabase} from '@/stores/NKJ/api_request.js';

// 부모로부터 전달된 이벤트를 정의합니다.
const emits = defineEmits(['fetchProductsCallback']);

const products = ref([]);
const selectedProduct = ref(null);

const fetchProducts = (bankId) => {
  fetchProductsFromDatabase(bankId)
    .then((data) => {
      products.value = data;
    })
};

</script>
<!-- // import ProductDetailModal from '@/components/fin_api/ProductDetailModal.vue'; -->
