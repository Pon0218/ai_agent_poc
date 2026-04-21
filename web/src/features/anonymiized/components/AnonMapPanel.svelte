<script lang="ts">
	const TYPE_MAP: Record<string, string> = {
		ORG: '組織',
		PERSON: '人物',
		DATE: '日期',
		NUM: '編號',
		ENT: '實體',
		LOC: '地點',
		EMAIL: '信箱',
		PHONE: '電話',
		IDCARD: '身分證'
	};

	function typeLabel(token: string): string {
		const m = token.match(/\[\[([A-Z]+)_\d+\]\]/);
		return m ? (TYPE_MAP[m[1]] ?? m[1]) : '—';
	}

	let {
		mappingTable = {}
	}: {
		mappingTable?: Record<string, string>;
	} = $props();

	let rows = $derived(
		Object.entries(mappingTable).map(([token, orig]) => ({
			token,
			original: orig.trim(),
			type: typeLabel(token)
		}))
	);
</script>

<div
	class="flex flex-1 flex-col overflow-hidden rounded-[10px] border border-s-background/18 bg-s-card-background"
>
	<!-- header -->
	<div
		class="flex shrink-0 items-center justify-between border-b border-s-background/18 bg-s-main px-3.5 py-2"
	>
		<div class="flex items-center gap-3">
			<div class="h-1.5 w-1.5 shrink-0 rounded-full bg-s-sub-headline"></div>
			<span class="text-[14px] tracking-[1.2px] text-s-sub-headline uppercase"
				>匿名化對應表 (anon map)</span
			>
		</div>
		<span class="text-[10px] text-s-sub-headline">—</span>
	</div>

	<!-- table -->
	<div class="flex-1 overflow-auto">
		<table class="w-full text-[12px]">
			<thead class="sticky top-0">
				<tr class="border-b border-s-background/18">
					{#each ['原始值', '替換 token', '類型', '信心度'] as col (col)}
						<th
							class="bg-s-card-background px-3 py-1.25 text-left text-[12px] font-normal tracking-[0.9px] text-s-sub-headline uppercase"
						>
							{col}
						</th>
					{/each}
				</tr>
			</thead>
			<tbody>
				{#if rows.length === 0}
					<tr>
						<td colspan="4" class="px-3 py-3 text-[14px] text-s-sub-headline">
							執行 pipeline 後顯示匿名化對應…
						</td>
					</tr>
				{:else}
					{#each rows as row (row.token)}
						<tr class="border-t border-s-background/5">
							<td class="px-3 py-2 text-s-background">{row.original}</td>
							<td class="px-3 py-2 text-[11px] text-s-tertiary">{row.token}</td>
							<td class="px-3 py-2 text-s-sub-headline">{row.type}</td>
							<td class="px-3 py-2 text-s-sub-headline">—</td>
						</tr>
					{/each}
				{/if}
			</tbody>
		</table>
	</div>
</div>
