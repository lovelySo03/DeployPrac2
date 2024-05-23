<template>
  <div class="first">
    <br>
  </div>
  <div class="exchange-container">
    <div class="card">
      <div class="card-body">
        <h2 class="card-title">환율 계산기</h2>
        <br>
        <form @submit.prevent="calculateFx" class="form">
          <div class="middle2">
            <div class="middle">
            <div class="form-group1">
                <label for="exchange-method">환전 방식</label>
                <select v-model="selected_Fx_Path" @change="fetch_Fx_Rate" id="exchange-method">
                  <option v-for="Fx_path in Fx_paths" :key="Fx_path.id" :value="Fx_path.path">{{ Fx_path.name }}</option>
                </select>
              </div>
              <div class="form-group2">
                <label for="currency">화폐 선택</label>
                <select v-model="selected_Fx_Nation" @change="fetch_Fx_Rate" id="currency">
                  <option v-for="Fx_nation in Fx_nations" :key="Fx_nation.id" :value="Fx_nation.name">{{ Fx_nation.name }}</option>
                </select>
              </div>
          </div>
          <div class="form-group3">
            <label for="amount">보내는 돈</label>
            <input type="text" v-model="Fx_me" id="amount">
          </div>
          </div>
        </form>
  
        <div class="middle3">
            <div class="form-group4">
              <!-- <div>
                <p>&nbsp;환율 </p>
              </div> -->
              <div>
                <p class="result" style="color: rgb(255, 16, 28);">{{ Fx_result }}</p>
              </div>
            </div>
          <div class="form-group5">
            <form @submit.prevent="calculateFx" class="form">
            <button type="submit" class="btn-submit">계산</button>
          </form>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/NKJ/Fx_api';


const Fx_me = ref(0);
const Fx_Now = ref([]);
const selected_Fx_Path = ref('ttb');
const selected_Fx_Nation = ref('미국 달러');
const Fx_result = ref(0);
const store = useCounterStore();

const calculateFx = async () => {
  try {
    Fx_Now.value = await store.fetch_Fx_rate();
    for (let i = 0; i < Fx_Now.value.length; i++) {
      const currency = Fx_Now.value[i].cur_nm;
      if (currency === selected_Fx_Nation.value) {
        const rate = Fx_Now.value[i].ttb;
        Fx_result.value = (Number(rate.replace(/,/g, '')) / Number(Fx_me.value)).toFixed(2);
        break;
      }
    }
  } catch (error) {
    console.error('Error calculating exchange rate:', error);
    Fx_result.value = '환율 정보를 가져오는 중에 오류가 발생했습니다.';
  }
};

const Fx_paths = [
  { id: 1, name: '송금 보낼 때', path: 'ttb' },
  { id: 2, name: '송금 받을 때', path: 'tts' },
  { id: 3, name: '매매 기준율', path: 'deal_bas_r' },
];

const Fx_nations = [
  { id: 1, name: '미국 달러' },
  { id: 2, name: '한국 원' },
  { id: 3, name: '바레인 디나르' },
  { id: 4, name: '브루나이 달러' },
  { id: 5, name: '캐나다 달러' },
  { id: 6, name: '스위스 프랑' },
  { id: 7, name: '위안화' },
  { id: 8, name: '덴마아크 크로네' },
  { id: 9, name: '영국 파운드' },
  { id: 10, name: '홍콩 달러' },
  { id: 11, name: '인도네시아 루피아' },
  { id: 12, name: '일본 옌' },
  { id: 13, name: '호주 달러' },
  { id: 14, name: '쿠웨이트 디나르' },
  { id: 15, name: '말레이지아 링기트' },
  { id: 16, name: '노르웨이 크로네' },
  { id: 17, name: '뉴질랜드 달러' },
  { id: 18, name: '사우디 리얄' },
  { id: 19, name: '스웨덴 크로나' },
  { id: 20, name: '싱가포르 달러' },
  { id: 21, name: '태국 바트' },
  { id: 22, name: '아랍에미리트 디르함' },
];
</script>

<style scoped>

.first {
  height: 20vh;
}
.exchange-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.card {
  width: 70%;
  border: 3px solid  #4CAF50; 
  border-radius: 10px; 

}

.card-body {
  padding: 20px;
}

.form-group1 {
  margin-bottom: 20px;
  margin-top: 10px;
}

.form-group2 {
  margin-bottom: 20px;
}

.form-group3 {
  margin-bottom: 20px;
  margin-left: 5px;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn-submit {
  /* background-color: #1089FF; */
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.result {
  margin-top: 20px;
  font-size: 1.5rem;
  font-weight: bold;
  color: #4CAF50; 
  text-align: center;
}

.middle {
  display: flex;
  justify-content: space-between; 
  align-items: center;
}

/* .middle3 {
  display: flex;
  justify-content: space-between; 
  align-items: center;
} */

/* .form-group4 {
  display: flex;
  align-items: flex-start; 
  justify-content: space-between; 
  gap: 20px; 
} */

.form-group4 {
  display: flex;
  justify-content: center; 
  
}

.middle > * {
  flex: 1; 
  margin: 0 5px; 
}

.middle2 > * + * {
  margin-top: 10px;
}

.btn-submit {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: auto; 
  margin-right: 10px; 
}

.form-group4 > div > p {
  font-family: inherit;
  font-weight: bold; 
}

.form-group4 > div:first-child > p {
  color: rgb(16, 137, 255); 
}

.card-title {
  color: #4CAF50;
  /* background-color: rgb(246,199,189); */
}
</style>