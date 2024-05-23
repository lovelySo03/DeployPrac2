<template>
  <div class="total">
    <h2 class="header"></h2>
    <div class="middle1">
      <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#savingSection" aria-expanded="false" aria-controls="savingSection">
      적금 목록
      </button>
      &nbsp;
      <button class="btn btn-danger" type="button" data-bs-toggle="collapse" data-bs-target="#depositSection" aria-expanded="false" aria-controls="depositSection" @click="toggleSavingSection(false)">
      예금 목록
      </button>

    </div>
    <!-- 적금 목록 -->
    <br>
    <div class="collapse" id="savingSection">
    <!-- <h1 class="product-title">적금 목록</h1> -->
    <div class="product-section">
      <table class="product-table saving-table">
        <thead>
          <tr>
            <th>상품명</th>
            <th>금리(1개월)
              <button @click="sortProducts('saving', '1', 'asc')">↑</button>
              <button @click="sortProducts('saving', '1', 'desc')">↓</button>
            </th>
            <th>금리(3개월)
              <button @click="sortProducts('saving', '3', 'asc')">↑</button>
              <button @click="sortProducts('saving', '3', 'desc')">↓</button>
            </th>
            <th>금리(6개월)
              <button @click="sortProducts('saving', '6', 'asc')">↑</button>
              <button @click="sortProducts('saving', '6', 'desc')">↓</button>
            </th>
            <th>금리(12개월)
              <button @click="sortProducts('saving', '12', 'asc')">↑</button>
              <button @click="sortProducts('saving', '12', 'desc')">↓</button>
            </th>
            <th>금리(24개월)
              <button @click="sortProducts('saving', '24', 'asc')">↑</button>
              <button @click="sortProducts('saving', '24', 'desc')">↓</button>
            </th>
            <th>금리(36개월)
              <button @click="sortProducts('saving', '36', 'asc')">↑</button>
              <button @click="sortProducts('saving', '36', 'desc')">↓</button>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in savingProducts" :key="product.id" @click="showProductDetail(product)">
            <td>{{ product.fin_prdt_nm }}</td>
            <td>{{ getInterestRate(product, '1') }}</td>
            <td>{{ getInterestRate(product, '3') }}</td>
            <td>{{ getInterestRate(product, '6') }}</td>
            <td>{{ getInterestRate(product, '12') }}</td>
            <td>{{ getInterestRate(product, '24') }}</td>
            <td>{{ getInterestRate(product, '36') }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
    
    <!-- 예금 목록 -->
    <!-- <h1 class="product-title">예금 목록</h1> -->

    <div class="collapse" id="depositSection">
    <div class="product-section">
      <table class="product-table deposit-table">
        <thead>
          <tr>
            <th>상품명</th>
            <th>금리(1개월)
              <button @click="sortProducts('deposit', '1', 'asc')">↑</button>
              <button @click="sortProducts('deposit', '1', 'desc')">↓</button>
            </th>
            <th>금리(3개월)
              <button @click="sortProducts('deposit', '3', 'asc')">↑</button>
              <button @click="sortProducts('deposit', '3', 'desc')">↓</button>
            </th>
            <th>금리(6개월)
              <button @click="sortProducts('deposit', '6', 'asc')">↑</button>
              <button @click="sortProducts('deposit', '6', 'desc')">↓</button>
            </th>
            <th>금리(12개월)
              <button @click="sortProducts('deposit', '12', 'asc')">↑</button>
              <button @click="sortProducts('deposit', '12', 'desc')">↓</button>
            </th>
            <th>금리(24개월)
              <button @click="sortProducts('deposit', '24', 'asc')">↑</button>
              <button @click="sortProducts('deposit', '24', 'desc')">↓</button>
            </th>
            <th>금리(36개월)
              <button @click="sortProducts('deposit', '36', 'asc')">↑</button>
              <button @click="sortProducts('deposit', '36', 'desc')">↓</button>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in depositProducts" :key="product.id" @click="showProductDetail(product)">
            <td>{{ product.fin_prdt_nm }}</td>
            <td>{{ getInterestRate(product, '1') }}</td>
            <td>{{ getInterestRate(product, '3') }}</td>
            <td>{{ getInterestRate(product, '6') }}</td>
            <td>{{ getInterestRate(product, '12') }}</td>
            <td>{{ getInterestRate(product, '24') }}</td>
            <td>{{ getInterestRate(product, '36') }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

    <product-detail-modal :selectedProduct="selectedProduct" v-if="selectedProduct" @close="closeProductDetail" />
  </div>
</template>

<script setup>
import { defineProps, ref, watch } from 'vue';
import ProductDetailModal from './ProductDetailModal.vue';

const props = defineProps(['products']);

const selectedProduct = ref(null);
const savingProducts = ref(props.products?.saving_products || []);
const depositProducts = ref(props.products?.deposit_products || []);

const showProductDetail = (product) => {
  selectedProduct.value = product;
};

const closeProductDetail = () => {
  selectedProduct.value = null;
};

const getInterestRate = (product, term) => {
  const option = product.options.find(opt => opt.save_trm === term);
  return option ? parseFloat(option.intr_rate) : null;
};

const sortProducts = (type, term, order) => {
  const products = type === 'saving' ? savingProducts : depositProducts;
  products.value.sort((a, b) => {
    const rateA = getInterestRate(a, term);
    const rateB = getInterestRate(b, term);

    if (rateA === null && rateB === null) return 0;
    if (rateA === null) return 1;
    if (rateB === null) return -1;

    return order === 'asc' ? rateA - rateB : rateB - rateA;
  });
};

const toggleSavingSection = (isOpen) => {
  const savingSection = document.getElementById('savingSection');
  if (savingSection) {
    const isSavingSectionOpen = savingSection.classList.contains('show');
    if (isOpen && !isSavingSectionOpen) {
      savingSection.classList.add('show');
    } else {
      savingSection.classList.remove('show');
    }
  }
};

// selectedProduct의 변경을 감지하여 옵션을 업데이트
watch(() => props.products, (newVal) => {
  savingProducts.value = newVal.saving_products || [];
  depositProducts.value = newVal.deposit_products || [];
}, { deep: true });
</script>
<style scoped>

.header {
  text-align: center;
  color:  #e91e63;

 }


.total {
  margin-left: 5%;
  margin-right: 3%;
  font-weight: 900; 
}

.header {
  margin-bottom: 20px;
}

.product-section {
  margin-bottom: 40px;
}

.product-title {
  font-size: 24px;
  margin-bottom: 10px;
}

.saving-table thead tr {
  background-color: blue;
  color: white;
}

.deposit-table thead tr {
  background-color:red; 
  color: white;
}

.product-table {
  width: 100%;
  border-collapse: collapse;
}

.product-table th,
.product-table td {
  padding: 8px;
  text-align: center;
  border: 1px solid #ccc;
}

.product-table th {
  font-weight: bold;
}

.saving-table tbody tr:hover {
  /* background-color: #005bff;
  color: white; */

  background-color: rgb(248,220,196);
  color: black;
}

.deposit-table tbody tr:hover {
  /* background-color: #ff5757; 
  color: white; */

  background-color:  rgb(248,220,196);
  color: black;

}

.product-table button {
  border: none;
  background: none;
  cursor: pointer;
  color: white;
}

.product-table button:hover {
  color: blue;
}

.middle1 {
  margin-left:5%;
}
</style>
