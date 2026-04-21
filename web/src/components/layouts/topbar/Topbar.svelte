<script lang="ts">
	import { getContext } from 'svelte';
	import FaviconSvg from '@/assets/favicon.svg?component';

	const ctx = getContext<{ reset: () => void }>('app');
</script>

<header class="flex h-16.5 w-full items-center border-b border-s-stroke/50 bg-s-background px-3">
	<button
		onclick={ctx.reset}
		class="flex cursor-pointer items-center gap-[11.37px] rounded-lg px-[9.1px] py-[5.68px] transition-opacity hover:opacity-70 active:scale-95"
	>
		<FaviconSvg class="size-5.75" />
		<span class="font-['Playfair_Display'] text-[22.74px] leading-[28.42px] text-s-headline">
			ProductLens
		</span>
	</button>
</header>
