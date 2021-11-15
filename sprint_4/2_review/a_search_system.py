def search(docs, requests):
    docs_words = []
    for index in range(len(docs)):
        docs_words.append({})
        for word in docs[index].split():
            docs_words[index][word] = docs_words[index].get(word, 0) + 1
    result = []
    for request_index in range(len(requests)):
        result.append({index: 0 for index in range(len(docs))})
        for index in range(len(docs)):
            for word in set(requests[request_index].split()):
                if word in docs_words[index]:
                    result[request_index][index] += docs_words[index][word]
    result = [
        [item[0]+1 for item in sorted(
            result[index].items(), key=lambda item: (-item[1], item[0])
        ) if item[1] > 0]
        for index in range(len(result))
    ]
    return '\n'.join(
        ' '.join(str(element[index]) for index in range(5))
        if len(element) >= 5
        else ' '.join(str(element[index]) for index in range(len(element)))
        for element in result
    )


def test_search():
    result = search(
        [
            'i love coffee', 'coffee with milk and sugar',
            'free tea for everyone',
        ],
        [
            'i like black coffee without milk', 'everyone loves new year',
            'mary likes black coffee without milk',
        ],
    )
    assert result == '1 2\n3\n2 1', f'Wrong answer: {result}'
    result = search(
        [
            'buy flat in moscow', 'rent flat in moscow', 'sell flat in moscow',
            'want flat in moscow like crazy',
            'clean flat in moscow on weekends', 'renovate flat in moscow',
        ],
        [
            'flat in moscow for crazy weekends', 'flat', 'flat in',
        ],
    )
    assert result == '4 5 1 2 3\n1 2 3 4 5\n1 2 3 4 5', (
        f'Wrong answer: {result}'
    )
    result = search(
        [
            'buy flat in moscow', 'rent flat in moscow', 'sell flat in moscow',
            'want flat in moscow like crazy',
            'clean flat in moscow on weekends', 'renovate flat in moscow',
        ],
        [
            'flat in moscow for crazy weekends', 'flat', 'flat in',
        ],
    )
    assert result == '4 5 1 2 3\n1 2 3 4 5\n1 2 3 4 5', (
        f'Wrong answer: {result}'
    )
    result = search(
        [
            'yqrl lllll',
            'oeudtlqdk tvvug fkwg ivf aiwgp dhv zybtyojul cwyh skfhmfgl lv hmwo lhndnztr luh fwvzv cpr gog',
            'wlialru zaui dnqyowqg jbzziggzg xyer mg axey jrxb rhmsckbag usof au lrtnsv ykvkz oy odxrcrdykk',
            'lxalfrnya chkcrrvau dswpb opznrto jjwaskhxja mepfrx fh yurkret etjs jnlze dtvzq kt ma dx knb',
            'wq qewwplk ny aqzvd naxw uou ekfqfmid vpub usnt fztqw koic gakm tzupyaryc dfnlmjgy fwfcbnerno',
        ],
        [
            'qdaugqbwhx yqrl rapnell wq wq irlzv jrwgibds fjxkibzo cwcjdrii lntm nvjcox uytgfpxa foamnezsoc',
        ],
    )
    assert result == '1 5', f'Wrong answer: {result}'
    result = search(
        [
            'iaszkhjoak lml okn copjfnmyg nxyqf dqegnckxrc mreawpgksu xu tdtt mg jvlsovvkw bcijmm wpobmir',
            'suvg cdokvnrlv autkcvo xmzvmskvz ua wo oipkx qgtdhnmtoo dtecmiuf ivlyk gs ztszz jvlsovvkw pfmipny',
            'kzoraga kniyhayzrb mreawpgksu lktelnzfc pxrwr jrwgibds aqnjfaeuam xiubvw qgfkni peccmimhr ydix',
            'euy wugonfndb rtmks imkige pkqlsvbh pyv jyszayle zvbvf bis opbj arfur peccmimhr brlpeqq pvuqfc',
            'rxntg cinoshf fcfcer gsnics vncnkvk hi cwcqumcjhu gnr zfpix zhkr chkcrrvau beu cfwvnay bbxprt',
            'qrdjir hosbbyos tbb cfipdz jhpnizt tzwuhlzcw dq wdadqts xo it at cqkz xoiiasq jcdbpitph rqwwgiqs',
            'ieopkmp dxvt vsfhasjv hjdatyst qvttu oaapik zj gvqyk oaapik esgqpk bsmts tffrnxztmv mpfxvf',
            'hiuwmkh zgoys kzoraga osejhjrjbg qsqhm qmdu usnt qnxpg xjkmia iaszkhjoak tiaveof vifmuleo bxrnatzu',
            'gecxvtgrdf uqvvb mekcylar binohp pa dqegnckxrc ivvxynhqui kvxbvn smvzoxxu kvjv fgwtlyp oco',
            'ibiplpbdeq untkeumy jddryfqohu mbbji svjv qbfwyd cfjdnei zllufh ch zqjjnj auxyzrrv kikkzej',
            'zixaxjjb ieopkmp gbkhskq etrpjuaulg qxofsaslwp ujrho kvaxzcblo srsijaops bfkm zxqg sh rmkws',
            'fu epextjxzk nrvmbcqcr ny tzupyaryc ovkczj rmkws jjwaskhxja sljeoshpxl kmil bcupdjq oigngby',
            'cqeey nec myz bwnmwsp dxe cwyh ay riihjdf hxcxpzq gpmno hi uetomlo ieawft jydozyqmap onuhtupja',
            'lhkpctoog jyszayle jossvcj oigngby nqpjatrull hebzjd tu lop lksqhr uy vet keigxemgyr oylzzfljls',
            'ulyypz mujf ovkczj ttndw tffrnxztmv ozz jgynicb rbubbw sytla ktswsfnb pjrry zgead afexauy ndprn',
            'xrmbi zcwwc aiwgp pklqhahtmf bpdhcabq tlcj qzcgtisv ndprn uoykq ycxolh lcpxp mpv auxyzrrv kgazeulbwb',
            'zwgha arfur dkhukxm zkgkqja xjkmia pklqhahtmf zsxfwii sh ilsoxihozl nyo cuzyzdrz chgu gmcmaishc',
            'vxdqxnqnvn amkz unracmkc fjkdjxvtq xrmbi cqeey lbadhufl ktfuvsl lhu pkqlsvbh gbkhskq zqjjnj',
            'oy jkqqhfuub zikmiqqu wdadqts kxwkrbq jgynicb ltdhcqah fpemxcnvv mpv ldxqonejed pfsavpgc vsfhasjv',
            'pklqhahtmf qhiqx hwpe bu gs luqyfndtvi rmvgsaksks nojfj qgtdhnmtoo cqeey ctas oaapik lm ckutg',
            'oh gqz cqkz ilgzea qgfkni pklqhahtmf yurb ukcurvcc tzupyaryc rcf snzusfvrp qvttu bmn vnwctsxb',
            'ldxqonejed unefx knb hs scpplnlqqd gpmno oy vxdqxnqnvn zxt fr edsv onuhtupja xiubvw dgn ktswsfnb',
            'htibaplqa dx wkjnocbbsv rvg sytla kbkottunq wjsfwr fbmgliu sxip becdpytu lm zataekerig lk qewwplk',
            'seogoip ld tqjxwupw uzfmw lumec jgynicb snzusfvrp hkr rhpboijexc eekpqndcr rqlz zmlsrruycj',
            'hosbbyos ha wpobmir kdgzj rgcqsm xml thvsuoop iaszkhjoak cwcjdrii zemhwvg udefqgiqn hlfecj',
            'pnclkaadoo autkcvo ck upuzd dibe usxfsilsfi bmn menwmnmphq yeuqpp jd xdatgbrb ed hfuzkj rtt',
            'ecmgcynb jkqqhfuub ypioqq rhpboijexc nsqzyl wsgpjlei nuiyc sljeoshpxl ojvfjf vphawgsxya rmwuzbd',
            'gfaox enyxt duk ck iqq yeuqpp jddryfqohu yokjhcuys qmconkpike pvhy pkgncwjn jg kevth mdkcumpioz',
            'onuhtupja zgobmtaauz gpwgpg hwreiua pxrxz smvzoxxu wtujidre pdcbhldu ivlyk uqiwvoqcf errdn',
            'la gmav errdn la jxtyfimw lv fh hgmgmoizkm edsv pkgncwjn zsxfwii ciuksxvdji wijgllawe tvvug',
            'wpxloc vifmuleo oaapik yaaneisx rqwwgiqs kplj mwkwwor oh ynzc vuml bbyvjjbncf htibaplqa tzcksuzb',
            'suywicbqm ycsgocoab kneaikd vvgcdo hkegg thvsuoop jsuibndpmc ztszz oaapik qpoh rqlz suywicbqm',
            'gwpc ycxolh rxktljpxlf jg hbrnoanoe ekinplthn dhv jpdcnghv fwvzv ttgpvbhpf zemhwvg bcupdjq',
            'su rmkws bcupdjq xogrewqjg mppekxykkb wkjnocbbsv swiwhbzhaw kowm mx usnt jakpaaqv whzbrpc hi',
            'dxe ed pjrry jdg ldxqonejed lv ekinplthn rbgrgvkqa ftpreoi avgqcwae gbmkcrq qutn foamnezsoc',
            'nsg udioljbyrv dhv pkgncwjn mig usx brxi pypakybfl etjs lgnp bxyvbkhu hopgzfq ot qhbpbp ygkpazs',
            'cgkabirxum alh rbubbw uqt tvrzs braintlqy cqkz lrz eekpqndcr wugonfndb lbadhufl vbsbanumvj',
            'xsh bis nt bp snzusfvrp fjusuavhx bfkm qhbpbp zllufh cwcjdrii fwfcbnerno vamatlcb unefx mhtrq',
            'pypakybfl vfckbuqwsw xvzrypbkya rclopnmc ywdqlgypse nbeht lvwjeypov jqudb nojfj ta gd zqjjnj',
            'nsqbo uqt ij fjxkibzo ttndw qxofsaslwp uqjgqz zn zikmiqqu lxcrr gnr rmwuzbd ubgx lgnp idwix',
            'qmlhypnpi nrvmbcqcr uyzcjae eycxywan mwkwwor nxyqf ukzxptzglc xi ydmpx qiddegnz gfaox dgrsxfqw',
            'hkr inyxgt fyqbmnhv xc vyusbmrqq bpodwwapc wz fzgcsla mx lhu sbqzt ndxksjrft dtvzq qndftxz',
            'arfur scuejrtyt cqeey qdaugqbwhx gmcmaishc wsgpjlei oleeorlsxc iomloqjn folabwflbb kneaikd',
            'irtozr ilgzea npknhrst bsyef ui dxejsjhsjq fjxkibzo zgobmtaauz dhv usof ecyxdxa nuiyc fdup',
            'ilsoxihozl ttgpvbhpf ci irtozr ay zxzdlmtas nec kobsz widdkejv thvsuoop iycmwaw dolxnxn ovkczj',
            'smvzoxxu dm flg cfwvnay igloi xml kzpdwzxr vphawgsxya iycmwaw zj gs shjtdz kplj gs ilgzea dxejsjhsjq',
            'eoyhd ivvxynhqui jsuibndpmc kx wdadqts sytla cwcjdrii idwix pkgncwjn udefqgiqn namfc tvrzs',
            'mekcylar lop cqeey kxewwvudim kuofyxt hcxkmgmypj djspktt nz wdadqts zmlsrruycj xsh iqq prjnpjgfta',
            'aqzvd aq fkwg wugonfndb kmk qndftxz yhf zvtsvvq wtujidre kte smvzoxxu brlpeqq vsfhasjv euy',
            'rygei kvxbvn uqjgqz uqiwvoqcf ijbw iierhyhlq zxguducdg qj zkw usx errdn bxbkzm ta otabjmkgfr',
            'rxktljpxlf bp hmwo twixfvprqt ekfqfmid qhiqx gd qdaugqbwhx ot bmn oyobypfa msb ziaarb bcbjgn',
            'okn ooydxyxbo gfaox yk cwyh pojolywazy zvbvf pgspsxr ueajeek xfjuupqn ov oemxovjctb hbacto',
            'bp fpvelv pxrxz vygpuby zzeudjkrs gmeqemu pefbxugju vplyq hepxpdnm hdpvbj ms wberp oeudtlqdk',
            'ogvwi qeprrbtdwe dx urggbvvs dgn svyqwvx rfifkwucub brxi zvbvf hxcxpzq qksrq kvadwc ehzzgd',
            'fgwtlyp tnxmzmghiy dq ay evrgrpdtk qxofsaslwp cbrxnqjxo ywdqlgypse qewwplk xdbj ijwd hgapysh',
            'gevestgz ozz txno qosk qewwplk no yauystmn byfsl hs ojvfjf opbj xh gecxvtgrdf mocfna pgspsxr',
            'jcdbpitph tpbubrtbh bdybymxin bmpt vx hbrnoanoe lz fbbhdnpibr it cfwvnay aq tzcksuzb ltmuis',
            'ieopkmp guw tj pcan tdtt guv vamatlcb cinoshf zybtyojul nqjln ciuksxvdji car shywniswkh ulyr',
            'ny aa qp qj iqq zsxfwii qbtcjc zxzdlmtas scuejrtyt unefx kmil rvryh ynzc kuofyxt ozz lccusmfe',
            'ppxuivk gkks fzwy vfckbuqwsw zixaxjjb lop dtvzq dolxnxn phqvnyun lntm pnclkaadoo hmwo fdsbpjbq',
            'pfsavpgc yoiwsxb xfwagw yd ma rmwuzbd ta rgcqsm tffrnxztmv gb fitwelokqk xfwagw untkeumy miohyz',
            'qewwplk irtozr hlbshhucx tbb chtbhknj qosk svjv gakm no uoknvow nrvmbcqcr hbrnoanoe hepxpdnm',
            'zmlsrruycj yk xbik whzbrpc rclopnmc drjk vyhp jj fr jsuibndpmc bsmts ff vixkzagv luh mkmri',
            'zaui seogoip vqigzfdh oyobypfa gs ncz deqa qmdu ukfhafoj znex urggbvvs cg eycxywan rlaxz mepfrx',
            'xl hobtoljz rekjff errdn rtmks mbsu ndauyx hepxpdnm scuejrtyt no vixkzagv ycxolh raookcu bpodwwapc',
            'cuzyzdrz luh nhuusjqik ltdhcqah ydmpx zcwwc odxrcrdykk gmcmaishc myk hiezqbkbi ndauyx kyctmyq',
            'uih ov hjdatyst esxtroaq becdpytu dx pneigx dtecmiuf jibtawabu msb jxtyfimw ydqa vqujgkdgy',
            'ny oco pa gog axmetzrca foamnezsoc yyxnpdiky hdpvbj jbrucdw aquzr qewwplk lu ivf djl lexwapjf',
            'usof cwh ydmpx mhtrq tzcksuzb bkujmb gpdvlve jtd cfjdnei lplzdo pelbzab rlaxz raookcu lzqljtmsbs',
            'hbrnoanoe vbsbanumvj tbb fyyhaf qndftxz tdtt rmvgsaksks zhkr ezcywfabrk edicza vxdqxnqnvn chkcrrvau',
            'fjusuavhx mujf fyyhaf os hkr axmetzrca ykumrbbmnj wjsfwr okmc fbbhdnpibr byicoeoxpx lk ck jhme',
            'lxalfrnya chkcrrvau dswpb opznrto jjwaskhxja mepfrx fh yurkret etjs jnlze dtvzq kt ma dx knb',
            'wlialru zaui dnqyowqg jbzziggzg xyer mg axey jrxb rhmsckbag usof au lrtnsv ykvkz oy odxrcrdykk',
            'oeudtlqdk tvvug fkwg ivf aiwgp dhv zybtyojul cwyh skfhmfgl lv hmwo lhndnztr luh fwvzv cpr gog',
            'gxl bwxsyqbsig jhpnizt qohz uqvvb bxyvbkhu dxejsjhsjq dibe phtpdop dexcpyxxs muq jsg sxip xvzrypbkya',
            'wq qewwplk ny aqzvd naxw uou ekfqfmid vpub usnt fztqw koic gakm tzupyaryc dfnlmjgy fwfcbnerno',
            'jthad zsbz evrgrpdtk mekcylar fwvzv ha mujf dqkhxreti vwdka ohm qxzxnrqstm vwqvleul ygkpazs',
            'nk oylzzfljls lxalfrnya drjk dohgvnyeh abu hjdatyst uaqqkta ycsgocoab jhme mchcjjxvu cojp qxofsaslwp',
            'untkeumy oy skfhmfgl dbdw hxcxpzq jwfgcjm yd xgnja jkqqhfuub nizetso zlzt knb qpoh ieopkmp',
            'zgunzv mg fkwg lgnp myz xjhhi cqeey mepfrx tvrrwbulw drbpn hhlyl mqwl ha hbrnoanoe myz dqanxbw',
            'vphawgsxya ycpmsqy iaiysrgc zxguducdg sljeoshpxl rtmks io uoykq ov axey pxrxz ixmdzbsghu scedmx',
            'aqzkwmudy hkhbzcbt tvvug zaui xo tlcj irtozr fsveb bbxprt fjkdjxvtq jkqqhfuub alqsrdpf iycmwaw',
            'suywicbqm npknhrst suywicbqm nrvmbcqcr cgfr bwnmwsp qp zxbk xtqqvxtz rfifkwucub wzsaa kx amrhqf',
            'vigu ua scpplnlqqd ftpreoi cfipdz qhiqx unracmkc otabjmkgfr ilgzea cheowwjcve exqxnpzbq ukzxptzglc',
            'gqz cqkz foamnezsoc oco ycsgocoab yk cinoshf njsfc aubgi njsfc mwkwwor uyugmlh pvhy rlaxz ezcywfabrk',
            'gt afexauy zaui srsijaops rgcqsm mepfrx cfkdbj mqwl qmlhypnpi jr yjmpwt pvhy ykvkz sytla vphawgsxya',
            'ywdqlgypse rqlz cwcqumcjhu vuml rrmtlnbf mzwyax gfdiupt ydix ibiplpbdeq yrza qeprrbtdwe foamnezsoc',
            'brlpeqq oleeorlsxc kqdctsaj vgp nt alqsrdpf vxdqxnqnvn gb cbtdvx mtrm gsnics zsaqiiinyy pkgncwjn',
            'fqr chkcrrvau pfsavpgc rqlz pxrwr vnwctsxb zzbvzegy ukcurvcc fu fbmgliu ulyr guw gyqkbfp gfaox',
            'unxqejcjpp vsfhasjv hsemz ilsoxihozl qywmmryymu afqdyw ydmpx gpdvlve oaapik xgpyd xvcravf nsqbo',
            'rclopnmc mrdvtq xjamrq ukfhafoj gxl idwix xdbj ltmuis yaaneisx rhpboijexc aqbxwhc krxri hqccg',
            'beu lcpxp flg mlijkcn hjdatyst xbrawjpaa mekcylar yauystmn hwpe lhkpctoog tzupyaryc oaapik',
            'hjdatyst hwreiua xyer hflrsqq ivk yaaneisx kuofyxt oeudtlqdk kkikgwhcy okn goamezrr afexauy',
            'gfdiupt fyqbmnhv gyqkbfp pxrwr oemxovjctb oleeorlsxc jrwgibds hepxpdnm scedmx yvngqga bsmts',
            'jid no hlfecj uqt jj eycxywan jfxn ywdqlgypse lyvz ptxlfp svi jwo tvrrwbulw kvaxzcblo zgead',
            'kgazeulbwb kvxbvn cagitkpk lzqljtmsbs vyusbmrqq tnxmzmghiy scuejrtyt irlzv tvrrwbulw rfnpxc',
            'bxyvbkhu thvsuoop ldxqonejed qndftxz qdaugqbwhx prck lksqhr qutn rbubbw jnlze mbsu bxyvbkhu',
            'skqsvedoti tzcksuzb loj vbsbanumvj mlijkcn twixfvprqt axmetzrca ot rzv zsxfwii uyugmlh gnr',
            'jg kvxbvn fsogfg esgqpk cagitkpk ibiplpbdeq fpvelv hflrsqq zsxfwii sljeoshpxl nvjcox bwnmwsp',
            'vvbg ivvxynhqui wz scuejrtyt lntm jfajusegz jyszayle thvsuoop ukzxptzglc nxyqf lml ycsgocoab',
        ],
        [
            'qdaugqbwhx yqrl rapnell wq wq irlzv jrwgibds fjxkibzo cwcjdrii lntm nvjcox uytgfpxa foamnezsoc',
        ],
    )
    assert result == '3 25 35 38 40', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_search()
    count = int(input())
    docs = [input() for _ in range(count)]
    count = int(input())
    requests = [input() for _ in range(count)]
    print(search(docs, requests))
