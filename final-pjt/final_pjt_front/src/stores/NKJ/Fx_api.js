// import { createStore } from 'vuex';
import { defineStore } from 'pinia'
import axios from 'axios';
// api_request.js
export const useCounterStore = defineStore('counter', () => {
  async function fetch_Fx_rate() {
    try {
      // console.log(1)
      const response = await axios.get('http://127.0.0.1:8000/api/v1/SD/Fx/');
      console.log(response.data)
      console.log(response)
      return response.data;
    } catch (error) {
      console.error('Error fetching products from database:', error);
      throw error;
    }
  }

  return { fetch_Fx_rate }
})

