<script lang="ts">
	import { onMount } from 'svelte';
	import './layout.css';
	import favicon from '@/assets/favicon.svg?url';
	import { enableMocking } from '@/testing/mocks'; // activates MSW request mocking in dev
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import { SvelteQueryDevtools } from '@tanstack/svelte-query-devtools'; // auto-stripped in production build
	import { queryClient } from '$lib/query-client';

	let { children } = $props();

	onMount(() => {
		enableMocking();
	});
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<!-- Provides the shared QueryClient instance to all child components -->
<QueryClientProvider client={queryClient}>
	{@render children()}
	<SvelteQueryDevtools />
</QueryClientProvider>
