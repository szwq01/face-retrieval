import request from '@/utils/request'

export function fetchDistance(distanceID) {
  return request({
    url: `/distances/${distanceID}`,
    method: 'get'
  })
}

export function fetchDistances(libraryID) {
  return request({
    url: '/distances',
    method: 'get',
    params: {
      libraryID
    }
  })
}

export function fetchLibraries() {
  return request({
    url: '/libraries',
    method: 'get'
  })
}

export function fetchLibrary(libraryName) {
  return request({
    url: `/libraries/${libraryName}`,
    method: 'get'
  })
}

export function fetchRetrieval(retrievalID) {
  return request({
    url: `/retrieves/${retrievalID}`
  })
}

export function createRetrieval(libraryID, distanceID, maxIterationFaces, maxIteration, strategy, remark) {
  return request({
    url: `/retrieves`,
    method: 'post',
    data: {
      libraryID,
      distanceID,
      maxIterationFaces,
      maxIteration,
      strategy,
      remark
    }
  })
}
export function createIteration(retrievalID, no, selected) {
  return request({
    url: `/retrieves/${retrievalID}/iterations`,
    method: 'post',
    data: {
      no: no,
      selected: selected
    }
  })
}
export function fetchList(query) {
  return request({
    url: '/article/list',
    method: 'get',
    params: query
  })
}

export function fetchArticle(id) {
  return request({
    url: '/article/detail',
    method: 'get',
    params: {
      id
    }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/article/pv',
    method: 'get',
    params: {
      pv
    }
  })
}

export function createArticle(data) {
  return request({
    url: '/article/create',
    method: 'post',
    data
  })
}

export function updateArticle(data) {
  return request({
    url: '/article/update',
    method: 'post',
    data
  })
}
