<script lang="ts">
	import { page } from '$app/state';
	import KeyboardArrowDown from '@material-symbols/svg-400/outlined/keyboard_arrow_down.svg?component';

	let { children } = $props();

	const routes = [
		{ label: 'anonymized-chat', path: '/anonymized-chat' },
		{ label: 'anonymized-image-file', path: '/anonymized-image-file' }
	];

	let open = $state(false);
	let container: HTMLElement;

	let currentLabel = $derived(
		routes.find((r) => page.url.pathname.startsWith(r.path))?.label ?? 'Strong → anon'
	);

	function handleWindowClick(e: MouseEvent) {
		if (open && container && !container.contains(e.target as Node)) {
			open = false;
		}
	}
</script>

<svelte:window onclick={handleWindowClick} />

<div class="mx-auto flex min-h-screen max-w-300 flex-col items-start gap-3 p-6">
	<!-- ── Nav ─────────────────────────────────────────────────────────────── -->
	<nav class="flex flex-col gap-3">
		<p class="text-[12px] tracking-[1.6px] text-s-sub-headline uppercase">
			anonymized llm gateway
		</p>

		<!-- Select menu -->
		<div class="relative" bind:this={container}>
			<!-- Trigger -->
			<button
				onclick={() => (open = !open)}
				class="inline-flex cursor-pointer flex-row items-center justify-center gap-3 border-b border-s-sub-headline px-3 py-2"
			>
				<span class="text-[20px] text-s-background">
					{currentLabel}
				</span>
				<KeyboardArrowDown class="size-4 fill-s-background" />
			</button>

			<!-- Menu list -->
			{#if open}
				<div
					class="absolute top-full left-0 z-10 flex w-full flex-col gap-3 bg-white p-3"
					style="box-shadow: 0px 10px 15px -3px rgba(0,0,0,0.1), 0px 4px 6px -2px rgba(0,0,0,0.05);"
				>
					{#each routes as route (route.path)}
						<a
							href={route.path}
							onclick={() => (open = false)}
							class="cursor-pointer text-left text-[16px] leading-6 tracking-[0.15px] text-s-background transition-opacity hover:opacity-70"
						>
							{route.label}
						</a>
					{/each}
				</div>
			{/if}
		</div>
	</nav>

	{@render children()}
</div>
