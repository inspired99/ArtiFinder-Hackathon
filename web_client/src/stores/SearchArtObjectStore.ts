import { defineStore } from 'pinia';
import { reactive } from 'vue';

export const useSerchArtObjectStore = defineStore('SerchArtObjectStore', () => {
  const searchItem = reactive<Partial<{
    title: string;
    description: string;
    image: File;
    imageUrl: string;
    path: string;
    category: string;
  }>>({});

  const uploadImage = async () => {
    const formData = new FormData();

    if (searchItem?.image) {
      formData.append('file', searchItem.image);
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });
      
      if (!response.ok) {
        throw new Error('Failed to upload image');
      }

      const data = await response.json();
      searchItem.path = data.path;
      console.log(data);
      return data;
    }

    return null;
  };

  const search = async () => {
    const response = await fetch('/api/get_arts_info', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: searchItem?.title,
        path: searchItem?.imageUrl,
        category: searchItem?.category,
      }),
    });
    const data = await response.json();
    return data;
  };

  return {
    searchItem,
    uploadImage,
    search,
  };
});
