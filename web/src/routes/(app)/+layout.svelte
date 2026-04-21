<script lang="ts">
	import { Topbar } from '@/components/layouts/topbar';

	let { children } = $props();
</script>

<div class="flex min-h-screen flex-col">
	<Topbar />
	<main class="flex flex-1 flex-col bg-s-background">
		{@render children()}
	</main>
</div>
