<template>
  <div>
    <h2 class="text-h4 mb-4">{{ isEdit ? 'Edit Trip' : 'Add New Trip' }}</h2>
    <v-form @submit.prevent="saveTrip">
      <v-row>
        <v-col cols="12">
          <v-text-field
            v-model="trip.name"
            label="Trip Name"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-textarea
            v-model="trip.description"
            label="Description"
            rows="3"
          ></v-textarea>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="trip.transport"
            label="Transport"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="trip.location"
            label="Location"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="trip.hotel"
            label="Hotel"
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-textarea
            v-model="trip.attractions"
            label="Attractions"
            rows="3"
          ></v-textarea>
        </v-col>
        <v-col cols="12" class="d-flex gap-4">
          <v-btn
            color="primary"
            type="submit"
          >
            {{ isEdit ? 'Update Trip' : 'Create Trip' }}
          </v-btn>
          <v-btn
            color="secondary"
            variant="text"
            @click="router.push('/')"
          >
            Cancel
          </v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import type { Trip, TripFormData } from '@/types/trip'

const props = defineProps<{
  id?: string
}>()

const router = useRouter()
const trip = ref<TripFormData>({
  name: '',
  description: '',
  transport: '',
  location: '',
  hotel: '',
  attractions: ''
})

const isEdit = computed(() => !!props.id)

const fetchTrip = async () => {
  if (!props.id) return
  
  try {
    const response = await axios.get<Trip>(`http://localhost:5000/api/trips/${props.id}`)
    const tripData = response.data
    trip.value = {
      name: tripData.name,
      description: tripData.description || '',
      transport: tripData.transport || '',
      location: tripData.location || '',
      hotel: tripData.hotel || '',
      attractions: tripData.attractions || ''
    }
  } catch (error) {
    console.error('Error fetching trip:', error)
  }
}

const saveTrip = async () => {
  try {
    if (isEdit.value) {
      await axios.put(`http://localhost:5000/api/trips/${props.id}`, trip.value)
    } else {
      await axios.post('http://localhost:5000/api/trips', trip.value)
    }
    router.push('/')
  } catch (error) {
    console.error('Error saving trip:', error)
  }
}

onMounted(() => {
  if (isEdit.value) {
    fetchTrip()
  }
})
</script> 