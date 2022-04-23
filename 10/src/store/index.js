import { createStore } from 'vuex'

export default createStore({
  state: {
    users: [{"value":"3","key":1650737061390,"role":1},{"value":"4","key":1650737062321,"role":0},{"value":"1","key":1650737059105,"role":0},{"value":"5","key":1650737064305,"role":0}],
  },
  mutations: {
    addUser(state, data) {
      state.users = data;
    }, 
  },
  actions: {
  },
  modules: {
  }
})
