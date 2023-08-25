<script lang="ts">
  let isOpen = false;
  let selectedLanguage = "it";
  const languages = [
    { name: "Italiano", icon: "🇮🇹" },
    { name: "Inglese", icon: "🇬🇧" },
  ];

  function toggleDropdown() {
    isOpen = !isOpen;
  }

  function selectLanguage(language: string) {
    selectedLanguage = language;
    isOpen = false;
    dispatch('locale-changed', language );
  }
    // old

    import {
      createEventDispatcher
    } from 'svelte';
    //export let value = 'en';
    const dispatch = createEventDispatcher();
  /*
    // @ts-ignore
    function switchLocale(event) {
      event.preventDefault();
      dispatch('locale-changed', selectedLanguage );
    }
    //event.target.value
    */
  </script>
  <!--
  <style>
    .choose-locale {
      display: flex;
      justify-content: center;
    }
  

  </style>

  <div class="choose-locale ">
    <div> <select value={value} on:change={switchLocale} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg border-l-gray-100 dark:border-l-gray-700 border-l-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
        <option value="en">EN</option>
        <option value="it">IT</option>
      </select> </div>
  </div>

  class="h-10 px-3 bg-gray-200 hover:bg-gray-300 rounded flex items-center"


  <span class="mr-2">🇬🇧</span>
    <span>English</span>


    aria-hidden="true" class="h-4 w-4 mr-2"
-->   

<div class="relative">
  <button
    class="flex-shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-500 bg-gray-100 border border-gray-300 rounded-full hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600"
    on:click={toggleDropdown}
  >
  {#if selectedLanguage == "it"}
  
  <div class="inline-flex items-center">
    <span class="rounded-full mr-2"> 🇮🇹 </span>     
    Italiano <svg aria-hidden="true" class="w-4 h-4 ml-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
  </div>
  {/if}
  {#if selectedLanguage == "en"}
  
  <div class="inline-flex items-center">
    <span class="rounded-full mr-2">🇬🇧</span>
    English <svg aria-hidden="true" class="w-4 h-4 ml-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
  </div>
{/if}
  </button>
  {#if isOpen}
  <div class="absolute right-0 mt-2 w-48 bg-white border rounded shadow-lg z-10">

    <button
      value = "it"
      class="inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white"
      on:click={() => selectLanguage("it")}
    >
    <div class="inline-flex items-center">
      <span class="rounded-full mr-2"> 🇮🇹 </span> 
      Italiano
    </div>
    </button>
    <button
    value = "en"
    class="inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white"
    on:click={() => selectLanguage("en")}
  >
  <div class="inline-flex items-center">
    <span class="rounded-full mr-2">🇬🇧</span>
   English
</div>
  </button>
  </div>
  {/if}
</div>




