<script lang="ts">
	import { buildSegments } from '../utils/buildSegments';

	let {
		error = null,
		result,
		mappingTable = {},
		deanonymizationOk = true,
		deanonymizationFalseReasons = []
	}: {
		error?: string | null;
		result?: string;
		mappingTable?: Record<string, string>;
		deanonymizationOk?: boolean;
		deanonymizationFalseReasons?: string[];
	} = $props();

	let segments = $derived(result != null ? buildSegments(result, mappingTable) : []);
</script>

<div
	class="flex min-h-40 w-full flex-col gap-3 overflow-hidden rounded-[10px] border border-s-sub-headline bg-s-main px-3 py-2"
>
	<!-- header -->
	<div class="flex w-full items-center justify-between border-b border-s-background/18 px-3 py-2">
		<div class="flex items-center gap-3">
			<div class="h-1.5 w-1.5 shrink-0 rounded-full bg-s-background"></div>
			<span class="text-[12px] tracking-[1.2px] text-s-sub-headline uppercase"
				>最終結果（反匿名化後）</span
			>
		</div>
		<span class="text-[12px] text-s-sub-headline">hover 還原詞查看原始 token</span>
	</div>

	<!-- content -->
	<div class="min-h-9.75 px-3 py-2 text-[14px] leading-5.75 text-s-sub-headline">
		{#if error}
			<span class="text-s-tertiary">{error}</span>
		{:else if segments.length > 0}
			{#if !deanonymizationOk}
				<span class="text-[12px] text-s-tertiary"
					>⚠ 反匿名化未完全成功：{deanonymizationFalseReasons.join('、')}</span
				>
				<br />
			{/if}
			{#each segments as seg, i (i)}
				{#if seg.token}
					<span
						class="group relative inline-block cursor-default rounded bg-s-card-background px-1 text-s-background"
					>
						{seg.text}
						<span
							class="pointer-events-none absolute bottom-full left-1/2 z-10 mb-1 -translate-x-1/2 rounded bg-s-background px-2 py-1 text-[10px] whitespace-nowrap text-s-main opacity-0 transition-opacity group-hover:opacity-100"
						>
							{seg.token}
						</span>
					</span>
				{:else}
					{seg.text}
				{/if}
			{/each}
		{:else}
			<span class="opacity-60">pipeline 執行後，還原的回應將顯示於此…</span>
		{/if}
	</div>
</div>
