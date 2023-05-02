<template>
  <div id="app">
    <h1>{{ title1 }}</h1>
    <h2>{{ title2 }}</h2>
    <h3>{{ title3 }}</h3>
    <div class="time-grid">
      <button v-for="time in times" :key="time" :class="{'selected': selectedTimes.includes(time) }" @click="toggleTime(time)">
        {{ time }}
      </button>
    </div>
    <hr class="blue">
    <div class="bold">
      선택 시간 : {{ selectedTimes.join(' ') }}
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {
    
  },
  data() {
    return {
      title1: '버튼 박스 제작',
      title2: '예약 페이지',
      title3: '시간 선택',
      times: ["00:00","00:30","01:00","01:30","02:00","02:30","03:00","03:30","04:00","04:30","05:00","05:30","06:00","06:30","07:00","07:30","08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectedTimes: []
    }
  },
  methods: {
    toggleTime(time) {
      const index = this.selectedTimes.indexOf(time)
      if (index === -1) { // 선택한 적이 없을 때
        if (this.selectedTimes.length < 5) { // 5개보다 적게 선택했을 떄
          this.selectedTimes.push(time) 
        }
      } else { // 이미 앞에서 선택한 적이 있음
        this.selectedTimes.splice(index, 1)
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Noto Sans Korean;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #424242;
  margin-top: 60px;
}

.time-grid {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  grid-gap: 10px;
  margin-top: 20px;
}

button {
  width: 100%;
  height: 50px;
  border: none;
  background-color: white;
  font-size: 16px;
  color: #84898C;
  cursor: pointer;
}

.selected {
  background-color: #bed9ff;
  color: #0F4C81;
}

hr {
  background: #0F4C81;
  height: 1px;
  border: 0;
}

.bold {
  font-weight: bold;
}
</style>
