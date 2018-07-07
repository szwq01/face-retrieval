<template>
  <el-row type="flex" justify="center" style="padding:20px;">
    <el-col :span="8" :xs="{span:24}">
      <el-form ref="form" :model="form" :rules="rules" label-width="110px">
        <el-form-item required label="图片库" prop="libID">
          <el-select @change="updateDistances" v-model="form.libID" placeholder="请选择图片库">
            <el-option v-for="lib in libraries" :label="lib.name" :value="lib.id"></el-option>
          </el-select>
        </el-form-item>
        <!-- <el-form-item label="特征算法">
          <el-select v-model="form.region" placeholder="请选择活动区域">
            <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option>
          </el-select>
        </el-form-item> -->
        <el-form-item required label="特征距离" prop="distance">
          <el-select v-model="form.distance" placeholder="请特征距离">
            <el-option v-for="dis in distances" :label="dis.name" :value="dis.id"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item required label="选择策略" prop="strategy">
          <el-select v-model="form.strategy" placeholder="请选择策略">
            <el-option v-for="strategy in strategies" :label="strategy.label" :value="strategy.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item required label="供选人像数" prop="maxIterationFaces">
          <el-select v-model="form.maxIterationFaces" placeholder="请选择人像数">
            <el-option v-for="option in facesOptions" :label="option.label" :value="option.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item required label="反馈次数上限" prop="maxIteration">
          <el-input-number v-model="form.maxIteration" :min="1" :max="10" label="描述文字"></el-input-number>
        </el-form-item>
        <el-form-item label="备注" prop="remark">
          <el-input type="textarea" v-model="form.remark"></el-input>
        </el-form-item>
        <!-- <el-form-item label="即时配送">
          <el-switch v-model="form.delivery"></el-switch>
        </el-form-item>
        <el-form-item label="活动性质">
          <el-checkbox-group v-model="form.type">
            <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
            <el-checkbox label="地推活动" name="type"></el-checkbox>
            <el-checkbox label="线下主题活动" name="type"></el-checkbox>
            <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item label="特殊资源">
          <el-radio-group v-model="form.resource">
            <el-radio label="线上品牌商赞助"></el-radio>
            <el-radio label="线下场地免费"></el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="活动形式">
          <el-input type="textarea" v-model="form.desc"></el-input>
        </el-form-item> -->
        <el-form-item>
          <el-button @click="resetForm('form')">重置</el-button>
          <el-button type="primary" @click="submitForm('form')">立即创建</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
</template>


<script>
import { fetchLibraries, fetchDistances, createRetrieval } from '@/api'
export default {
  data() {
    return {
      libraries: [],
      distances: [],
      facesOptions: [{ label: 8, value: 8 }, { label: 12, value: 12 }, { label: 16, value: 16 }, { label: 24, value: 24 }],
      strategies: [{ label: '随机', value: 'random' }, { label: '最相似', value: 'similarity' }, { label: '墒算法', value: 'randon' }],
      form: {
        libID: '',
        distance: '',
        strategy: 'random',
        maxIterationFaces: 8,
        maxIteration: 8,
        remark: ''
      },
      rules: {
        libID: [{ required: true, message: '请选择图片库', trigger: 'change' }],
        distance: [{ required: true, message: '请选择特征距离', trigger: 'change' }],
        maxIterationFaces: [{ type: 'number', required: true, message: '请输入供选人像数', trigger: 'change' }]
      }
    }
  },
  mounted() {
    fetchLibraries().then(resp => {
      this.libraries = resp.data
    })
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          createRetrieval(this.form.libID, this.form.distance, this.form.maxIterationFaces, this.form.maxIteration, this.form.strategy, this.form.remark).then(
            resp => {
              const retrievalID = resp.data.id
              this.$router.push(`/retrieval/${retrievalID}/start`)
              console.log(resp.data)
            }
          )
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
    updateDistances() {
      fetchDistances(this.form.libID).then(resp => {
        this.distances = resp.data
      })
    }
  }
}
</script>
