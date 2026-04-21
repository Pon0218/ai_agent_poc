<script lang="ts">
	import type { Snippet } from 'svelte';
	import Button from '@/components/ui/button/Button.svelte';

	let {
		charCount,
		onrun,
		onclear,
		isPending = false,
		disabled = false,
		children
	}: {
		charCount: number;
		onrun: () => void;
		onclear: () => void;
		isPending?: boolean;
		disabled?: boolean;
		children: Snippet;
	} = $props();
</script>

<div
	class="flex flex-1 flex-col rounded-[10px] border border-s-background/10 bg-s-card-background p-px"
>
	<!-- header bar -->
	<div
		class="flex items-center justify-between rounded-t-[10px] border-b border-s-background/10 bg-s-main px-3.5 py-2"
	>
		<div class="flex items-center gap-2">
			<div class="h-1.5 w-1.5 shrink-0 rounded-full bg-s-tertiary"></div>
			<span class="text-[14px] tracking-[1.2px] text-s-highlight uppercase">原始資料</span>
		</div>
		<span class="text-[14px] text-s-sub-headline">{charCount} chars</span>
	</div>

	<!-- body -->
	{@render children()}

	<!-- footer bar -->
	<div
		class="flex flex-row items-center gap-3 rounded-b-[10px] border-t border-s-background/10 bg-s-main px-3.5 py-3"
	>
		<Button onclick={onrun} {disabled} class="min-w-32 rounded-[5px]">
			{isPending ? '執行中…' : '執行 Pipeline'}
		</Button>
		<Button variant="ghost" onclick={onclear} class="min-w-32 rounded-[5px]">清除</Button>
	</div>
</div>
