export interface Trip {
  id: number;
  name: string;
  description?: string;
  transport?: string;
  location?: string;
  hotel?: string;
  attractions?: string;
}

export type TripInput = Omit<Trip, 'id'>;

export interface TripFormData {
  name: string;
  description: string;
  transport: string;
  location: string;
  hotel: string;
  attractions: string;
} 