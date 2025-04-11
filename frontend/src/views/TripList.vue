<template>
  <div>
    <v-row class="mb-4">
      <v-col cols="12" class="d-flex justify-end">
        <v-btn
          color="primary"
          prepend-icon="mdi-plus"
          @click="router.push('/trip/new')"
        >
          Add New Trip
        </v-btn>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-card v-for="trip in trips" :key="trip.id" class="mb-4">
          <v-card-title>{{ trip.name }}</v-card-title>
          <v-card-text>
            <p><strong>Description:</strong> {{ trip.description }}</p>
            <p><strong>Location:</strong> {{ trip.location }}</p>
            <p><strong>Transport:</strong> {{ trip.transport }}</p>
            <p><strong>Hotel:</strong> {{ trip.hotel }}</p>
            <p><strong>Attractions:</strong> {{ trip.attractions }}</p>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              variant="text"
              @click="router.push(`/trip/${trip.id}/edit`)"
            >
              Edit
            </v-btn>
            <v-btn
              color="error"
              variant="text"
              @click="deleteTrip(trip.id)"
            >
              Delete
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import type { Trip } from '@/types/trip'

const router = useRouter()
const trips = ref<Trip[]>([])

const fetchTrips = async () => {
  try {
    const response = await axios.get<Trip[]>('http://localhost:5000/api/trips')
    trips.value = response.data
  } catch (error) {
    console.error('Error fetching trips:', error)
  }
}

const deleteTrip = async (id: number) => {
  try {
    await axios.delete(`http://localhost:5000/api/trips/${id}`)
    await fetchTrips()
  } catch (error) {
    console.error('Error deleting trip:', error)
  }
}

onMounted(fetchTrips)
</script> 