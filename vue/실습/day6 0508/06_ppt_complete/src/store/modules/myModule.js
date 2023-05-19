const myModule = {
  state: {
    level: 20,
  },
  mutations: {
    INCREMENT_Level(state) {
      state.level += 1
    }
  },
  actions: {
    incrementLevel(context) {
      context.commit('INCREMENT_Level')
    }
  },
}

export default myModule
