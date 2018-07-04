// import { queryRule, removeRule, addRule } from '../services/api';

export default {
  namespace: 'retrieval',

  state: {
    iterations: [],
    options: {
      maxFaces: 16,
      maxIterations: 8,
    },
  },

  effects: {
    // *fetch({ payload }, { call, put }) {
    //   const response = yield call(queryRule, payload);
    //   yield put({
    //     type: 'save',
    //     payload: response,
    //   });
    // },
    // *add({ payload, callback }, { call, put }) {
    //   const response = yield call(addRule, payload);
    //   yield put({
    //     type: 'save',
    //     payload: response,
    //   });
    //   if (callback) callback();
    // },
    // *remove({ payload, callback }, { call, put }) {
    //   const response = yield call(removeRule, payload);
    //   yield put({
    //     type: 'save',
    //     payload: response,
    //   });
    //   if (callback) callback();
    // },
  },

  reducers: {
    // save(state, action) {
    //   return {
    //     ...state,
    //     data: action.payload,
    //   };
    // },
  },
};
