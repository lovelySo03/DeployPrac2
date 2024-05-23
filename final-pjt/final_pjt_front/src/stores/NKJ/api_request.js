import { createStore } from 'vuex';
import axios from 'axios';
export default createStore({
  state() {
    return {
      selectedBank: null,
      products: [],
      selectedProduct: null,
    };
  },
  mutations: {
    setSelectedBank(state, bankId) {
      state.selectedBank = bankId;
    },
    setProducts(state, products) {
      state.products = products;
    },
    setSelectedProduct(state, product) {
      state.selectedProduct = product;
    },
  },
  actions: {
    async fetchProducts({ commit, state }) {
      try {
        // 백엔드에서 데이터베이스에 접근하여 상품 정보를 가져옵니다.
        const products = await fetchProductsFromDatabase(state.selectedBank);
        // 상품 정보를 스토어에 저장합니다.
        commit('setProducts', products);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    },
    async fetchProductDetail({ commit }, productId) {
      try {
        // 백엔드에서 데이터베이스에 접근하여 특정 상품의 상세 정보를 가져옵니다.
        const product = await fetchProductDetailFromDatabase(productId);
        // 선택된 상품의 상세 정보를 스토어에 저장합니다.
        commit('setSelectedProduct', product);
      } catch (error) {
        console.error('Error fetching product detail:', error);
      }
    },
  },
});

// api_request.js

// 데이터베이스에서 상품 정보를 가져오는 함수
async function fetchProductsFromDatabase(selectedBank) {
  try {
    const url = selectedBank
    ?`http://127.0.0.1:8000/api/v1/SD/products/bank/${selectedBank}/`
    :'http://127.0.0.1:8000/api/v1/SD/products/all/'
    const response = await axios.get(url);
    console.log(url)
    console.log(response.data)
    return response.data;
  } catch (error) {
    console.error('Error fetching products from database:', error);
    throw error;
  }
}


// 데이터베이스에서 특정 상품의 상세 정보를 가져오는 함수
async function fetchProductDetailFromDatabase(productId) {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/SD/products/${productId}/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching product detail from database:', error);
    throw error;
  }
}

export { fetchProductsFromDatabase, fetchProductDetailFromDatabase };
