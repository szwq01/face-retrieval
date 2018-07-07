<template>
  <div style="padding:20px;">
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card shadow="always">
          当前人脸库：{{retrieval.library.name}}
          <br/> 特征：
          <br/> 距离：{{retrieval.distance.name}}
          <br/> 策略：{{retrieval.strategy}}
          <br/>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover">
          目标
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="never">
          图片库
        </el-card>
      </el-col>
    </el-row>
    <el-row :gutter="12">
      <el-col style="margin-top:10px;" :span="photoSpan" v-for="(photoName,index) in photos" :key="index">
        <photo-card :libraryName="libraryName" :photoName="photoName" @click.native="getNextIteration(photoName)"></photo-card>
      </el-col>
    </el-row>
    <el-row :gutter="12" style="margin-top:20px;" type="flex" justify="center">
      <el-col :span="4" :xs="{span: 6}">
        <el-button @click="back" :disabled="iterationPointer <= 1">返回</el-button>
      </el-col>
      <el-col :span="4" :xs="{span: 6}">
        <el-button type="primary">结束</el-button>
      </el-col>
    </el-row>
    <el-row :gutter="12" style="margin-top:20px;">
      <el-col :span="3" v-for="photoName in selectedHistory" :key="photoName">
        <photo-card :libraryName="libraryName" :photoName="photoName"></photo-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { createIteration, fetchRetrieval } from '@/api'
import photoCard from './components/photo'
export default {
  components: { photoCard },
  props: ['retrievalID'],
  data() {
    return {
      iterations: [],
      retrieval: {},
      iterationPointer: 0,
      selectedHistory: [],
      libraryName: 'orlimages'
    }
  },
  mounted: function() {
    fetchRetrieval(this.retrievalID).then(resp => {
      this.retrieval = resp.data
      this.getNextIteration('0')
    })
  },
  computed: {
    photos: function() {
      if (this.iterationPointer === 0) {
        return []
      } else {
        return this.iterations[this.iterationPointer - 1]
      }
    },
    photoSpan: function() {
      // if (this.photos.length === 48) {
      //   return 2
      // }
      return 48 / this.photos.length
    }
  },
  methods: {
    getNextIteration(selectedPhoto) {
      createIteration(this.retrievalID, this.iterationPointer, selectedPhoto).then(resp => {
        this.iterations.push(resp.data)
        this.iterationPointer && this.selectedHistory.push(selectedPhoto)
        this.iterationPointer += 1
      })
    },
    back() {
      this.iterationPointer -= 1
      this.selectedHistory.pop()
    }
  }
}
</script>
