<script lang="ts">
	import { Nav } from '@/components/layouts/nav';
	import { Footer } from '@/components/layouts/footer';

	let { children } = $props();
</script>

<div class="flex min-h-screen flex-col">
	<Nav />
	<main class="flex flex-1 flex-col">
		{@render children()}
	</main>
	<Footer />
</div>
